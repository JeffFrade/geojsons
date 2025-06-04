# GeoJSONs dos Distritos de SP e Principais Cidades do ABC Paulista
---

Esse projeto contempla os `GeoJSONs` dos distritos das seguintes cidades:

- São Paulo (`distritos-sp.geojson`).
- Santo André (`distritos-sa.geojson`).
- São Bernardo do Campo (`distritos-sbc.geojson`).
- São Caetano do Sul (`distritos-scs.geojson`).
- Diadema (`distritos-diadema.geojson`).

** Os `GeoJSONs` estão dentro da pasta `geojsons`.

### Scripts Python
---

Há 2 scripts Python no projeto que utilizei para corrigir alguns arquivos que obtive e estavam com dados incorretos ou fora de padrão de `geojson`, sendo eles:

- `fix-geojson.py` => Utilizado para corrigir GeoJSONs inválidos que obtive.
- `fix-coordinates.py` => Utilizado para conversão dos valores de latitude e longitude de UTM para 23S.

### Docker
---

Esse ponto é mais para desenvolvedores.
Criei um docker para subir o Python, instalar as dependências (`requirements.txt`) e executar os scripts Python.

#### Executando o Docker
---

Para executar o docker pela primeira vez:
```bash
docker compose up --build
```

Ele vai demorar um pouco, pois vai configurar tudo e rodar o script.

#### Demais Vezes
---

Se quiser rodar algum dos scripts que criei para trabalhar com arquivos ou criar novos, basta executar os seguintes passos:

- Trocar o `command` pelo script que deseja executar:
```yml
services:
  geo_converter:
    build: .
    volumes:
      - .:/app
    working_dir: /app
    command: python meu-script.py
```

- Se alterar algo no `Dockerfile` ou instalar uma nova dependência:
```bash
docker compose up --build
```

- Só criou um novo script e não alterou nada na estrutura do Docker:
```bash
docker compose up
```

Fique a vontade para fazer fork do projeto ou quiser adicionar mais `geojsons`, basta me chamar e adicionamos juntos.
