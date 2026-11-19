import enum

class OrderType(str, enum.Enum):
    dine_in = "dine_in"
    takeout = "takeout"
    delivery = "delivery"

class OrderStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    preparing = "preparing"
    ready = "ready"
    out_for_delivery = "out_for_delivery"
    completed = "completed"
    cancelled = "cancelled"

class PaymentMethod(str, enum.Enum):
    card = "card"
    cash = "cash"
    online = "online"

class PaymentStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"
    refunded = "refunded"