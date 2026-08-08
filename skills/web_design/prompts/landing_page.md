# Instrucciones de Diseño: Landing Page

## Estructura obligatoria (Above the fold → CTA)

```
1. HERO SECTION (viewport completo)
   - Headline: máximo 8 palabras, beneficio claro
   - Subheadline: 1-2 oraciones expandiendo el valor
   - CTA principal: botón contrastante, verbo de acción
   - Imagen/ilustración de soporte

2. SOCIAL PROOF (confianza)
   - Logos de clientes o "usado por X empresas"
   - Testimonios (foto + nombre + cargo)
   - Números de impacto (usuarios, países, uptime)

3. FEATURES/BENEFICIOS (3-4 máximo)
   - Ícono + título + descripción corta
   - Grid de 3 columnas en desktop, stack en mobile

4. HOW IT WORKS (proceso)
   - 3 pasos simples con números/íconos
   - Reducir fricción mental

5. PRICING (si aplica)
   - Máximo 3 planes
   - Destacar el recomendado
   - CTA en cada plan

6. FAQ (reducir objeciones)
   - 4-6 preguntas frecuentes
   - Accordion/collapsible

7. FOOTER CTA (última oportunidad)
   - Repetir CTA principal
   - Links: legal, contacto, redes
```

## Reglas de Diseño

- Mobile-first (diseñar para 375px primero, luego expandir)
- Tailwind CSS (utility-first, no CSS custom innecesario)
- Máximo 2 fonts (1 heading + 1 body)
- Paleta: 1 primario + 1 secundario + 1 acento + neutrales
- Spacing consistente (múltiplos de 4px: 4, 8, 16, 24, 32, 48, 64)
- Contraste mínimo 4.5:1 texto/fondo (WCAG AA)
- Imágenes con alt text descriptivo
- Botones mínimo 44x44px (touch target)
- Line-height body: 1.5-1.75 | headings: 1.1-1.3
- Max-width de texto: 65-75 caracteres por línea

## SEO obligatorio

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="[beneficio principal en 155 chars]">
<meta property="og:title" content="[título]">
<meta property="og:description" content="[descripción]">
<meta property="og:image" content="[imagen social]">
<link rel="canonical" href="[url]">
```

## Accesibilidad (WCAG 2.1 AA)

- Todos los `<img>` con `alt`
- Headings jerárquicos (h1 > h2 > h3, sin saltar)
- Focus visible en elementos interactivos
- `aria-label` en íconos sin texto
- Skip-to-content link
- No depender solo del color para transmitir información
