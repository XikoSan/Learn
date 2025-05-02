## Архитектура GPT (decoder-only)

- Вход: последовательность токенов → embedded + position
- Проходит через слои attention + FFN
- Output → логиты → softmax → следующий токен

### Блок attention:
- Query, Key, Value
- Механизм: "сходство" между токенами → веса

### Где это применимо?
- LangChain, agent loop, planning
