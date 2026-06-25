import random


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def simulate_mode(devices, relays, traffic_load, simulation_time, rssi_threshold, po_lora=True):
    seed = devices * 1000 + relays * 100 + traffic_load * 10 + simulation_time + abs(rssi_threshold)
    random.seed(seed + (1 if po_lora else 0))

    packets_sent = int(devices * (simulation_time / 3600) * traffic_load)

    received = 0
    lost = 0
    forwarded = 0
    collisions = 0
    total_latency = 0

    for _ in range(packets_sent):
        distance = random.random()
        rssi = -65 - distance * 55 + random.uniform(-4, 4)

        collision_prob = clamp((devices / 1000) + (traffic_load / 650), 0.02, 0.28)
        direct_success = clamp(0.98 - distance * 0.55 - collision_prob, 0.35, 0.95)

        if random.random() < direct_success:
            received += 1
            total_latency += random.uniform(80, 135)
            continue

        if po_lora and relays > 0 and rssi < rssi_threshold:
            relay_success = clamp(0.88 + relays * 0.045 - collision_prob * 0.45, 0.55, 0.96)
            relay_collision = clamp(collision_prob - relays * 0.035, 0.01, 0.20)

            if random.random() < relay_collision:
                collisions += 1

            if random.random() < relay_success:
                received += 1
                forwarded += 1
                total_latency += random.uniform(145, 230) + relays * 10
            else:
                lost += 1
        else:
            if random.random() < collision_prob:
                collisions += 1
            lost += 1

    pdr = round((received / packets_sent) * 100, 2) if packets_sent else 0
    latency = round(total_latency / received, 2) if received else 0
    collision_rate = round((collisions / packets_sent) * 100, 2) if packets_sent else 0
    throughput = round((received * 51) / simulation_time, 2) if simulation_time else 0
    relay_utilization = round(clamp((forwarded / max(1, received)) * 100, 0, 100), 2)

    return {
        "packet_delivery_ratio": pdr,
        "latency_ms": latency,
        "collision_rate": collision_rate,
        "throughput_kbps": throughput,
        "relay_utilization": relay_utilization,
        "packets_sent": packets_sent,
        "packets_received": received,
        "packets_lost": lost,
        "packets_forwarded": forwarded,
    }


def run_simulation(devices=100, relays=2, traffic_load=50, simulation_time=3600, rssi_threshold=-110):
    standard = simulate_mode(devices, 0, traffic_load, simulation_time, rssi_threshold, po_lora=False)
    po_lora = simulate_mode(devices, relays, traffic_load, simulation_time, rssi_threshold, po_lora=True)

    return {
        **po_lora,
        "standard_lorawan": standard,
        "po_lora": po_lora,
        "improvement": {
            "pdr_gain": round(po_lora["packet_delivery_ratio"] - standard["packet_delivery_ratio"], 2),
            "throughput_gain": round(po_lora["throughput_kbps"] - standard["throughput_kbps"], 2),
            "collision_reduction": round(standard["collision_rate"] - po_lora["collision_rate"], 2),
        },
    }