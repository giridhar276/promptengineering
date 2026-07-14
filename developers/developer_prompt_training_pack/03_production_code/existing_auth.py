from dataclasses import dataclass

@dataclass(frozen=True)
class CurrentUser:
    user_id: str
    role: str

def get_current_user() -> CurrentUser:
    return CurrentUser(user_id="user-1001", role="warehouse_user")
