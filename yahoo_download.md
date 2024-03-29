Формат для ссылки-запроса (будь то JS или Django);

```js
const LINK = 'https://query1.finance.yahoo.com/v7/finance/download/{TARGET}?period1={TIME1}&period2={TIME2}&interval={INTERVAL}&events={EVENT_TYPE}&includeAdjustedClose=true';
```

Where:

- `{TARGET}`: цель запроса, может быть компанией (например: Amazon -> `AMZN`), компания всегда 4 буквы, для указания валют цель выглядит немного по-другому:
  - например, рубль: `{RUB}=X`; валюта всегда 3 буквы, X не МЕНЯЕТСЯ!
    - ВАЛЮТЫ ВОЗВРАЩАЮТ ОТНОШЕНИЕ К ДОЛЛАРУ, ТО ЕСТЬ: USD/RUB (RUB=X) = 92.4950;
  - криптовалюты также обозначаются тремя буквами, но в цели также должны указывать конвертируемую валюту, то есть: {`BTC-USD`};
    - УЧИТЫВАЙТЕ, ЧТО КОНВЕРТАЦИЯ КРИПТОВАЛЮТ В ОБЫЧНЫЕ ВАЛЮТЫ ПРОИСХОДИТ В ТЕОРИИ, В СВОБОДНОМ ПОРЯДКЕ.

Yahoo!Finance обновляется примерно каждые 3-5 секунд;

`INVERVAL` может быть:

- `1d` (день)
- `1wk` (неделя)
- `1mo` (месяц)

`EVENTS` может быть:
- `history` (Historical Prices);
- `div` (Dividens Only);
- `split` (Stock Splits);
- `capitalGain` (Capital Gain);