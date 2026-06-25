# 🌐✨ PO-LoRa Research Simulator

<p align="center">
  <b>Protocol-Oblivious Relay-Assisted LoRaWAN Research Platform</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React.js-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/LoRaWAN-IoT%20Simulation-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  🚀 A cinematic web-based simulator for evaluating <b>Protocol-Oblivious Relay Forwarding</b> in LoRaWAN networks.
</p>

---

## 🎬 Project Preview

**PO-LoRa Research Simulator** is a complete research platform built to evaluate how relay-assisted forwarding can improve communication reliability in LoRaWAN-based IoT networks.

The system compares:

```text
📡 Standard LoRaWAN Direct Communication
vs
🌐 PO-LoRa Relay-Assisted Multi-Hop Forwarding
```

It includes a premium UI, simulation lab, topology visualization, analytics dashboard, experiment history, and automatic PDF report export.

---

## 🧠 Research Idea

LoRaWAN is widely used for low-power and long-range IoT communication. However, in real deployments, some devices may suffer from:

- 📉 Weak signal strength
- ❌ Packet loss
- 🧱 Obstructed communication
- 🌫️ Poor coverage
- 📡 Long distance from gateway

**PO-LoRa** introduces protocol-oblivious relay forwarding, where relay nodes forward packets without reading or modifying the application payload.

This makes the system more flexible, interoperable, and suitable for different IoT scenarios.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎬 Cinematic Splash Screen | Premium animated startup with gateway, relays, devices, packets, and system status |
| 📊 Dashboard | Research summary and key simulation metrics |
| 🧪 Simulation Lab | Configure devices, relays, traffic load, simulation time, and RSSI threshold |
| 🌐 Network Topology | Visual representation of gateway, relay nodes, and end devices |
| 📈 Analytics | Performance comparison between Standard LoRaWAN and PO-LoRa |
| 🕘 Experiment History | Stores previous simulation runs for comparison |
| 📄 PDF Export | Generates structured simulation reports |
| ⚡ FastAPI Backend | Handles simulation logic and API response |
| 💻 React Frontend | Modern interactive user interface |

---

## 🏗️ System Architecture

```text
PO-LoRa-Project
│
├── frontend / React.js
│   ├── 🎬 Cinematic Splash Screen
│   ├── 📊 Dashboard
│   ├── 🧪 Simulation Lab
│   ├── 🌐 Network Topology
│   ├── 📈 Analytics
│   ├── 🕘 Experiment History
│   └── 📄 PDF Report Export
│
└── backend / FastAPI
    ├── 🚀 Simulation API
    └── 📡 /simulate Endpoint
```

---

## 🛠️ Technology Stack

### 💻 Frontend

- ⚛️ React.js
- 🌐 React Flow
- 📈 Recharts
- 📄 jsPDF
- 🎨 CSS3
- 🔗 Axios
- 🎯 Lucide React Icons

### 🚀 Backend

- 🐍 Python
- ⚡ FastAPI
- 🔥 Uvicorn
- 📡 Simulation Logic

---

## ⚙️ Simulation Parameters

The simulator allows the user to configure:

```text
📱 Number of End Devices
📡 Number of Relay Nodes
🚦 Traffic Load Percentage
⏱️ Simulation Duration
📶 RSSI Threshold
```

Example scenario:

```text
Devices: 250
Relays: 3
Traffic Load: 80%
Simulation Time: 3600 seconds
RSSI Threshold: -105 dBm
```

---

## 📊 Evaluation Metrics

| Metric | Meaning |
|---|---|
| 📦 Packet Delivery Ratio | Percentage of successfully received packets |
| ⏱️ Latency | Average packet delay |
| ⚠️ Collision Rate | Percentage of packets affected by collisions |
| 🚀 Throughput | Successfully delivered data rate |
| 🔁 Relay Utilization | Usage level of relay nodes |
| 📡 Packet Statistics | Packets sent, received, lost, and forwarded |

---

## 📈 Sample PO-LoRa Simulation Results

| Metric | Value |
|---|---:|
| 📦 Packet Delivery Ratio | 61.92% |
| ⏱️ Average Latency | 135.63 ms |
| ⚠️ Collision Rate | 13.01% |
| 🚀 Throughput | 175.45 kbps |
| 🔁 Relay Utilization | 25.51% |
| 📤 Packets Sent | 20000 |
| 📥 Packets Received | 12385 |
| ❌ Packets Lost | 7615 |
| 🔄 Packets Forwarded | 3159 |

---

## 🔍 Standard LoRaWAN vs PO-LoRa

| Metric | Standard LoRaWAN | PO-LoRa | Improvement |
|---|---:|---:|---:|
| 📦 Packet Delivery Ratio | 46.14% | 61.92% | +15.78% |
| 🚀 Throughput | 130.73 kbps | 175.45 kbps | +44.72 kbps |
| ⚠️ Collision Rate | 15.52% | 13.01% | 2.51% reduced |
| ⏱️ Latency | 117.93 ms | 135.63 ms | Relay overhead |

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Bunny100806/PO-LoRa-Project.git
cd PO-LoRa-Project
```

---

## ⚡ Backend Setup

Go to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install fastapi uvicorn
```

Run backend server:

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## 💻 Frontend Setup

Open a new terminal and go to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run React app:

```bash
npm start
```

Frontend runs at:

```text
http://localhost:3000
```

---

## 📡 API Endpoint

The frontend sends simulation data to:

```text
POST /simulate
```

Example request:

```json
{
  "devices": 250,
  "relays": 3,
  "traffic_load": 80,
  "simulation_time": 3600,
  "rssi_threshold": -105
}
```

---

## 📄 PDF Report Export

After running a simulation, the system can generate a professional PDF report containing:

- 🧪 Simulation parameters
- 📊 Performance metrics
- 🔍 Standard LoRaWAN vs PO-LoRa comparison
- 📡 Packet-level statistics
- 🧠 Research interpretation
- 🏁 Final evaluation

---

## 🖥️ Application Pages

```text
🎬 Cinematic Splash Screen
📊 Dashboard
🧪 Simulation Lab
🌐 Network Topology
📈 Analytics
🕘 Experiment History
📄 PDF Report Export
```

---

## 🎯 Project Contribution

This project provides a practical simulation platform for studying relay-assisted LoRaWAN communication.

The main contribution is the development of a complete web-based simulator that demonstrates how protocol-oblivious relay forwarding can improve packet delivery ratio and throughput in dense IoT environments.

The system combines:

```text
Simulation + Visualization + Analytics + History + PDF Reporting
```

into one complete research application.

---

## 🔮 Future Work

Future improvements may include:

- 📡 Real LoRaWAN dataset integration
- 🌍 Live gateway data collection
- 🏙️ Larger smart-city simulation scenarios
- 🚗 Mobility models
- ☁️ Cloud deployment
- 🧪 Real IoT testbed validation
- 🧠 Advanced relay selection strategies

---

## 👨‍💻 Author

### 👨‍🎓 Sai Charitharth Nadigoti  
**B.Sc. Computer Engineering**

🎓 **Vistula University**  
Akademia Finansów i Biznesu Vistula  

📍 Warsaw, Poland  

---

## 📌 Project Status

```text
✅ Frontend Completed
✅ Backend Completed
✅ Simulation Engine Completed
✅ Network Topology Completed
✅ Analytics Completed
✅ Experiment History Completed
✅ PDF Export Completed
✅ Research Paper Completed
```

---

## 🏁 Final Conclusion

The **PO-LoRa Research Simulator** shows that relay-assisted forwarding can improve packet delivery ratio and throughput compared with standard LoRaWAN under the tested scenario.

Although relay forwarding introduces slight latency overhead, the improvement in reliability and throughput makes PO-LoRa useful for weak coverage areas, dense IoT deployments, and multi-hop LoRaWAN communication research.

---

<p align="center">
  <b>🌐 PO-LoRa Research Simulator — Built for IoT Network Research 🚀</b>
</p>