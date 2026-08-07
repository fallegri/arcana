"""
Escenarios de carga para TaskFlow — Locust.

Uso:
  locust -f agents/stress_testing/scenarios/taskflow_load.py \
    --host=http://localhost:8000 --headless \
    --users 50 --spawn-rate 5 --run-time 60s
"""

import random
import string

from locust import HttpUser, between, task


class TaskFlowUser(HttpUser):
    """Simula un usuario típico de TaskFlow."""

    wait_time = between(1, 3)

    def on_start(self):
        suffix = "".join(random.choices(string.ascii_lowercase, k=8))
        self.email = f"load_{suffix}@test.com"
        self.password = "LoadTest$2026"
        self.task_ids = []

        self.client.post("/auth/register", json={
            "nombre": f"User {suffix}",
            "email": self.email,
            "password": self.password,
        })

        resp = self.client.post("/auth/login", json={
            "email": self.email,
            "password": self.password,
        })
        if resp.status_code == 200:
            self.headers = {"Authorization": f"Bearer {resp.json()['token']}"}
        else:
            self.headers = {}

    @task(5)
    def list_tasks(self):
        self.client.get("/tasks", headers=self.headers, name="/tasks [LIST]")

    @task(3)
    def create_task(self):
        resp = self.client.post("/tasks", json={
            "titulo": f"Task {random.randint(1, 99999)}",
            "prioridad": random.choice(["baja", "media", "alta"]),
        }, headers=self.headers, name="/tasks [CREATE]")
        if resp.status_code == 201:
            self.task_ids.append(resp.json().get("id"))

    @task(2)
    def search_tasks(self):
        term = random.choice(["informe", "tarea", "revisar"])
        self.client.get(f"/tasks?search={term}", headers=self.headers, name="/tasks [SEARCH]")

    @task(1)
    def complete_task(self):
        if self.task_ids:
            tid = random.choice(self.task_ids)
            self.client.patch(f"/tasks/{tid}", json={"estado": "completada"},
                             headers=self.headers, name="/tasks/{id} [COMPLETE]")
