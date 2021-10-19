from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class StackFrame:
    topic: str
    description: str
    user: str
    date: datetime

    def serialize(self) -> str:
        return json.dumps({'user': self.user, 'topic': self.topic, 'description': self.description, 'date': str(self.date)})
