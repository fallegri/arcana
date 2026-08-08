# Mobile App — Arquitectura y Patrones

## Estructura del Proyecto (React Native + Expo)

```
src/
├── app/                    # Navegación (Expo Router / React Navigation)
│   ├── (tabs)/             # Tab navigator
│   ├── (auth)/             # Stack de autenticación
│   └── _layout.tsx         # Layout root
├── components/
│   ├── ui/                 # Componentes base (Button, Input, Card)
│   ├── forms/              # Formularios reutilizables
│   └── screens/            # Componentes específicos por pantalla
├── services/               # Lógica de negocio + API calls
├── hooks/                  # Custom hooks
├── store/                  # Estado global (Zustand/Redux)
├── utils/                  # Helpers
├── constants/              # Colores, endpoints, config
└── types/                  # TypeScript types
```

## Patrones Obligatorios

### Navegación
- Tab Navigator para secciones principales (máx 5 tabs)
- Stack Navigator dentro de cada tab
- Deep linking configurado
- Gestos de navegación nativos (swipe back)

### Estado
- Local state: useState para UI
- Server state: React Query / TanStack Query (cache + sync)
- Global state: Zustand (simple) o Redux Toolkit (complejo)

### Offline-First
- Cache de datos con AsyncStorage / MMKV
- Cola de operaciones pendientes (sync cuando hay red)
- Indicador visual de estado de conexión

### Performance
- FlatList / FlashList para listas (nunca ScrollView para listas largas)
- Imágenes optimizadas (expo-image)
- Lazy loading de pantallas
- Memoización (React.memo, useMemo, useCallback)

### UX Móvil
- Touch targets mínimo 44x44pt
- Feedback háptico en acciones importantes
- Pull-to-refresh en listas
- Skeleton loaders (no spinners genéricos)
- Bottom sheet para acciones contextuales
- Toast/Snackbar para feedback (no alert())

### Seguridad
- Tokens en SecureStore (no AsyncStorage)
- Certificate pinning para APIs críticas
- Biometric auth (FaceID/TouchID) para datos sensibles
- No logging de datos sensibles
