# Design System — Reglas de Diseño Visual

## Tipografía

| Elemento | Font | Peso | Tamaño | Line-height |
|----------|------|------|--------|-------------|
| H1 | Inter/Poppins | 700 (Bold) | 48px / 3rem | 1.1 |
| H2 | Inter/Poppins | 600 (Semi) | 36px / 2.25rem | 1.2 |
| H3 | Inter/Poppins | 600 | 24px / 1.5rem | 1.3 |
| Body | Inter/System | 400 (Regular) | 16px / 1rem | 1.6 |
| Small | Inter/System | 400 | 14px / 0.875rem | 1.5 |
| Button | Inter/System | 600 | 16px / 1rem | 1 |

## Paletas por Industria

### Restaurante / Gastronomía
- Primario: #D4451A (rojo cálido)
- Secundario: #F5A623 (dorado)
- Acento: #2D5016 (verde oliva)
- Background: #FFF8F0 (crema)
- Texto: #1A1A1A

### Tecnología / SaaS
- Primario: #4F46E5 (indigo)
- Secundario: #06B6D4 (cyan)
- Acento: #F59E0B (amber)
- Background: #F8FAFC (slate-50)
- Texto: #0F172A

### Salud / Bienestar
- Primario: #059669 (emerald)
- Secundario: #0EA5E9 (sky)
- Acento: #F97316 (orange)
- Background: #F0FDF4 (green-50)
- Texto: #1E293B

### Finanzas / Corporate
- Primario: #1E40AF (blue-800)
- Secundario: #0F766E (teal-700)
- Acento: #CA8A04 (yellow-600)
- Background: #FFFFFF
- Texto: #111827

### Educación
- Primario: #7C3AED (violet)
- Secundario: #2563EB (blue)
- Acento: #F59E0B (amber)
- Background: #FAF5FF (violet-50)
- Texto: #1F2937

## Spacing Scale (Tailwind)

| Token | Valor | Uso |
|-------|-------|-----|
| space-1 | 4px | Padding interno mínimo |
| space-2 | 8px | Gap entre elementos inline |
| space-3 | 12px | Padding de badges/pills |
| space-4 | 16px | Padding de botones, cards |
| space-6 | 24px | Gap entre secciones pequeñas |
| space-8 | 32px | Margen entre bloques |
| space-12 | 48px | Separación de secciones |
| space-16 | 64px | Padding de secciones principales |
| space-24 | 96px | Hero section padding |

## Componentes Base

### Botones
```
Primary: bg-primary text-white px-6 py-3 rounded-lg font-semibold hover:opacity-90
Secondary: border-2 border-primary text-primary px-6 py-3 rounded-lg font-semibold
Ghost: text-primary underline hover:no-underline
```

### Cards
```
Default: bg-white rounded-xl shadow-sm border p-6 hover:shadow-md transition
Featured: bg-primary/5 border-primary/20 rounded-xl p-6
```

### Forms
```
Input: w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-primary/20 focus:border-primary
Label: block text-sm font-medium text-gray-700 mb-1
Error: text-red-600 text-sm mt-1
```
