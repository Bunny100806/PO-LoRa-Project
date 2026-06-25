\# 🌐 PO-LoRa Research Simulator



A professional web-based research simulator for evaluating \*\*Protocol-Oblivious Relay-Assisted LoRaWAN communication\*\*.



The project compares \*\*Standard LoRaWAN\*\* with \*\*PO-LoRa relay-assisted forwarding\*\* using configurable simulation parameters, topology visualization, analytics, experiment history, and automatic PDF report generation.



\---



\## 📌 Project Overview



\*\*PO-LoRa Research Simulator\*\* is designed to study how protocol-oblivious relay forwarding can improve LoRaWAN-based IoT communication.



LoRaWAN is widely used in Internet of Things applications because it supports long-range and low-power communication. However, end devices located far from the gateway may experience weak signal strength, packet loss, and poor communication reliability.



This simulator demonstrates how relay-assisted forwarding can improve packet delivery, throughput, and network reliability in dense IoT environments.



\---



\## ✨ Key Features



\- 🎬 Premium cinematic splash screen

\- 📊 Interactive dashboard

\- 🧪 Simulation lab for experiment configuration

\- 🌐 Network topology visualization

\- 📈 Analytics and performance comparison

\- 🕘 Experiment history tracking

\- 📄 Automatic PDF report export

\- ⚡ React.js frontend

\- 🚀 FastAPI backend

\- 🔁 API-based simulation workflow



\---



\## 🧠 Research Focus



The main focus of this project is \*\*protocol-oblivious relay forwarding\*\*.



In this approach, relay nodes forward packets without understanding or modifying the application payload. This makes the method flexible for different IoT applications while improving coverage and reliability.



The simulator evaluates the performance difference between:



\- Standard LoRaWAN direct communication

\- PO-LoRa relay-assisted multi-hop forwarding



\---



\## 🏗️ System Architecture



```text

PO-LoRa-Project

│

├── frontend / React.js

│   ├── Dashboard

│   ├── Simulation Lab

│   ├── Network Topology

│   ├── Analytics

│   ├── Experiment History

│   └── PDF Export

│

└── backend / FastAPI

&#x20;   └── /simulate API endpoint

```



\---



\## 🛠️ Technologies Used



\### Frontend



\- React.js

\- React Flow

\- Recharts

\- jsPDF

\- Lucide React

\- Axios

\- CSS3



\### Backend



\- Python

\- FastAPI

\- Uvicorn

\- Simulation logic using Python



\---



\## ⚙️ Simulation Parameters



The simulator allows users to configure:



\- Number of end devices

\- Number of relay nodes

\- Traffic load percentage

\- Simulation duration

\- RSSI threshold



Example scenario:



```text

Devices: 250

Relays: 3

Traffic Load: 80%

Simulation Time: 3600 seconds

RSSI Threshold: -105 dBm

```



\---



\## 📊 Evaluation Metrics



| Metric | Description |

|---|---|

| Packet Delivery Ratio | Percentage of packets successfully received |

| Latency | Average packet delay |

| Collision Rate | Percentage of packets affected by collisions |

| Throughput | Successfully delivered data rate |

| Relay Utilization | Usage level of relay nodes |

| Packet Statistics | Packets sent, received, lost, and forwarded |



\---



\## 📈 Sample Simulation Results



| Metric | Value |

|---|---:|

| Packet Delivery Ratio | 61.92% |

| Average Latency | 135.63 ms |

| Collision Rate | 13.01% |

| Throughput | 175.45 kbps |

| Relay Utilization | 25.51% |

| Packets Sent | 20000 |

| Packets Received | 12385 |

| Packets Lost | 7615 |

| Packets Forwarded | 3159 |



\---



\## 🔍 Standard LoRaWAN vs PO-LoRa



| Metric | Standard LoRaWAN | PO-LoRa | Improvement |

|---|---:|---:|---:|

| Packet Delivery Ratio | 46.14% | 61.92% | +15.78% |

| Throughput | 130.73 kbps | 175.45 kbps | +44.72 kbps |

| Collision Rate | 15.52% | 13.01% | 2.51% reduced |

| Latency | 117.93 ms | 135.63 ms | Relay overhead |



\---



\## 🚀 How to Run the Project



\### 1. Clone the Repository



```bash

git clone https://github.com/Bunny100806/PO-LoRa-Project.git

cd PO-LoRa-Project

```



\---



\## ▶️ Backend Setup



Go to the backend folder:



```bash

cd backend

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate the virtual environment:



```bash

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install fastapi uvicorn

```



Run the backend:



```bash

python -m uvicorn app.main:app --reload

```



Backend runs at:



```text

http://127.0.0.1:8000

```



\---



\## 💻 Frontend Setup



Open a new terminal and go to the frontend folder:



```bash

cd frontend

```



Install dependencies:



```bash

npm install

```



Run the React app:



```bash

npm start

```



Frontend runs at:



```text

http://localhost:3000

```



\---



\## 📡 API Endpoint



The frontend sends simulation data to:



```text

POST /simulate

```



Example request body:



```json

{

&#x20; "devices": 250,

&#x20; "relays": 3,

&#x20; "traffic\_load": 80,

&#x20; "simulation\_time": 3600,

&#x20; "rssi\_threshold": -105

}

```



\---



\## 📄 PDF Report Export



After running a simulation, the user can export a PDF report containing:



\- Simulation parameters

\- Performance metrics

\- Standard LoRaWAN vs PO-LoRa comparison

\- Packet-level statistics

\- Research interpretation

\- Final evaluation



\---



\## 📸 Application Screens



The simulator includes the following pages:



\- Dashboard

\- Simulation Lab

\- Network Topology

\- Analytics

\- Experiment History

\- PDF Report Export



\---



\## 🎯 Project Contribution



This project provides a practical simulation platform for evaluating relay-assisted LoRaWAN communication. It shows how protocol-oblivious relay forwarding can improve packet delivery ratio and throughput in dense IoT environments.



The system combines simulation, visualization, analytics, history tracking, and report generation in one complete web application.



\---



\## 🔮 Future Work



Future improvements may include:



\- Real LoRaWAN dataset integration

\- Live gateway data collection

\- Larger-scale simulations

\- Mobility models

\- Cloud deployment

\- Real IoT testbed validation

\- Advanced relay selection strategies



\---



\## 👨‍💻 Author



\### Sai Charitharth Nadigoti  

B.Sc. Computer Engineering  



🎓 Vistula University  

Akademia Finansów i Biznesu Vistula  



📍 Warsaw, Poland  



\---



\## 📌 Project Status



```text

Project Status: Completed

Frontend: Completed

Backend: Completed

Simulation: Completed

Topology Visualization: Completed

Analytics: Completed

Experiment History: Completed

PDF Export: Completed

Research Paper: Completed

```



\---



\## 🏁 Conclusion



The PO-LoRa Research Simulator shows that relay-assisted forwarding can improve packet delivery ratio and throughput compared with standard LoRaWAN under the tested scenario.



Although relay forwarding introduces slight latency overhead, the improvement in reliability and throughput makes PO-LoRa useful for weak coverage and dense IoT deployments.

