```mermaid
erDiagram
    vehicles {
        int vehicle_id PK
        varchar(255) make
        varchar(255) model
        varchar(20) registration
        varchar(50) vehicle_type
        int max_payload
    }
    locations {
        int location_id PK
        int vehicle_id FK
        decimal(10_6) latitude
        decimal(10_6) longitude
        datetime timestamp
        int speed
    }
    cargo {
        int cargo_id PK
        int vehicle_id FK
        int current_load
        datetime last_updated
    }
    odometer_readings {
        int reading_id PK
        int vehicle_id FK
        int odometer_value
        datetime timestamp
    }
    vehicles ||--o{ locations : has
    vehicles ||--o{ odometer_readings : has
    vehicles ||--o{ cargo : has
