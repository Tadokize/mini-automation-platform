# Mini Automation Platform

Plataforma simplificada de automação baseada em eventos com suporte a IA.

## Sobre o projeto

O sistema permite cadastrar regras de automação que são disparadas automaticamente quando eventos chegam. Por exemplo: quando um usuário se cadastra, o sistema pode enviar um email, registrar um log ou processar os dados com IA.

## Arquitetura

Cliente HTTP
     ↓
FastAPI (API REST)
     ↓
Automation Engine
     ↓
Actions (log, ai_process, webhook)
     ↓
SQLite (banco de dados)


## Design Patterns utilizados

- **Observer Pattern** — o engine observa eventos e notifica as ações correspondentes
- **Strategy Pattern** — cada tipo de ação (`log`, `ai_process`) é uma estratégia intercambiável
- **Repository Pattern** — acesso ao banco de dados isolado via SQLAlchemy

## Tecnologias

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Anthropic Claude API

## Como rodar

### Pré-requisitos
- Docker instalado

### Subir o projeto
```bash
git clone https://github.com/Tadokize/mini-automation-platform.git
cd mini-automation-platform
docker compose up --build
```

Acesse a documentação em: http://localhost:8000/docs

## Endpoints

### Eventos
- `POST /events` — registra um novo evento e dispara automações
- `GET /events` — lista todos os eventos

### Regras
- `POST /rules` — cria uma regra de automação
- `GET /rules` — lista todas as regras
- `DELETE /rules/{id}` — remove uma regra

### Execuções
- `GET /executions` — lista o histórico de execuções

## Exemplos de uso

### Criar uma regra de log
```json
POST /rules
{
  "event_type": "user.registered",
  "action_type": "log",
  "action_config": "Novo usuário cadastrado"
}
```

### Criar uma regra com IA
```json
POST /rules
{
  "event_type": "ticket.created",
  "action_type": "ai_process",
  "action_config": "Classifique a prioridade deste ticket"
}
```

### Disparar um evento
```json
POST /events
{
  "event_type": "user.registered",
  "payload": {
    "name": "João",
    "email": "joao@email.com"
  }
}
```