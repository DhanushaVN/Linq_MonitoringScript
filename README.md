# System Metrics Monitoring Stack

### 1. docker-compose.yml - The Orchestrator
What it does:
- Defines and connects all Docker containers (InfluxDB, Grafana, and the metrics generator)
- Sets up networking between containers so they can communicate
- Configures container settings (ports, volumes, environment variables)
- Automatically starts all services in the correct order

Key configurations:
- Exposes Grafana on port 3000 and InfluxDB on port 8086
- Creates persistent storage for InfluxDB data
- Sets Grafana admin credentials (username: admin, password: admin)

### 2. send_metrics.py - The Data Generator
What it does:
- Creates sample system metrics (CPU, memory, disk usage)
- Runs continuously, generating new data every 5 seconds
- Sends metrics to InfluxDB in the correct format
- Logs all activity for troubleshooting

How it works:
1. Generates random values between realistic ranges:
   - CPU: 20-90%
   - Memory: 30-95%
   - Disk: 10-80%
2. Formats data for InfluxDB
3. Sends to InfluxDB's HTTP API

### 3. system_metrics.json - The Dashboard
What it contains:
- A ready-to-use Grafana dashboard with 3 panels
- Visualizations for CPU, memory, and disk usage
- Pre-configured queries that get data from InfluxDB

Dashboard features:
- Real-time updating charts
- Responsive layout that works on different screen sizes
- Time-range selectors for historical data
- Automatic refresh every few seconds

### 4. datasource.yml - The Data Connector
What it does:
- Automatically connects Grafana to InfluxDB
- Sets InfluxDB as the default data source
- Stores connection details (URL, database name)

Configuration details:
- Uses the InfluxDB container's internal network address
- Connects to the 'metrics' database
- Sets up proxy access mode

### 5. dashboard.yml - The Dashboard Loader
What it does:
- Automatically loads dashboards when Grafana starts
- Specifies where to find dashboard files
- Makes dashboards editable in the Grafana UI

Key settings:
- Looks for dashboards in /var/lib/grafana/dashboards
- Preserves dashboards when containers restart
- Allows modifications through the web interface

## How Everything Works Together

1. Data Generation
   send_metrics.py creates metrics and sends to InfluxDB

2. Data Storage
   InfluxDB stores metrics in 'metrics' database

3. Data Visualization
   Grafana connects via datasource.yml, queries InfluxDB, and displays in system_metrics.json dashboard

4. Automation
   docker-compose.yml manages the entire stack
   dashboard.yml ensures dashboards load automatically

## Getting Started

1. Start all services:
   docker-compose up -d --build

2. Access the dashboard:
   - Open http://localhost:3000
   - Login with username admin and password admin
   - View the "System Metrics" dashboard

3. View raw data:
   docker exec influxdb influx -execute 'SELECT * FROM metrics..system_metrics'

## Maintenance Tips

- To stop: docker-compose down
- To update: Change config files then docker-compose up -d --build
- To troubleshoot: Check logs with docker-compose logs

