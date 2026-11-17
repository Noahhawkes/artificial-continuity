"""PROMETHEUS public demonstration: evidence is not approval.
Synthetic data only. This script is not an authenticated approval service.
Run: python3 evidence_gate_demo.py
"""
def unsafe_gate(record):
    return bool(record.get("hits"))

def governed_gate(record):
    return (record.get("source_primary_verified") is True
            and record.get("attribution_verified") is True
            and record.get("temporal_order_verified") is True
            and record.get("human_signoff") == "APPROVED")

def run():
    rows = [{"id": f"FC-{i:03d}", "hits": ["synthetic-match"]}
            for i in range(1, 6)]
    assert sum(map(unsafe_gate, rows)) == 5
    assert sum(map(governed_gate, rows)) == 0
    forged = dict(rows[0], human_signoff="APPROVED")
    assert not governed_gate(forged)
    synthetic_all_flags = dict(forged, source_primary_verified=True,
        attribution_verified=True, temporal_order_verified=True)
    assert governed_gate(synthetic_all_flags)
    print("PASS: 4 assertions; synthetic fixture; 0 historical ground truths adjudicated")
if __name__ == "__main__":
    run()
