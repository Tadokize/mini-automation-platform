from sqlalchemy.orm import Session
from app.models.rule import Rule
from app.models.execution import Execution
from app.models.event import Event

class AutomationEngine:
    def __init__(self, db: Session):
        self.db = db

    def process_event(self, event: Event):
        rules = self.db.query(Rule).filter(
            Rule.event_type == event.event_type,
            Rule.active == True
        ).all()

        for rule in rules:
            self._execute_rule(event, rule)

    def _execute_rule(self, event: Event, rule: Rule):
        try:
            result = self._run_action(rule.action_type, rule.action_config, event)
            status = "success"
        except Exception as e:
            result = {"error": str(e)}
            status = "error"

        execution = Execution(
            event_id=event.id,
            rule_id=rule.id,
            status=status,
            result=result
        )
        self.db.add(execution)
        self.db.commit()

    def _run_action(self, action_type: str, action_config: str, event: Event):
        if action_type == "log":
            print(f"[LOG] Evento: {event.event_type} | Config: {action_config}")
            return {"message": f"Log registrado: {action_config}"}

        elif action_type == "ai_process":
            from app.actions.ai_action import run_ai_action
            return run_ai_action(action_config, event.payload)

        else:
            return {"message": f"Ação '{action_type}' executada"}