def compute_iou(box1: list[float], box2: list[float]) -> float:
    inter_x1 = max(box1[0], box2[0])
    inter_y1 = max(box1[1], box2[1])
    inter_x2 = min(box1[2], box2[2])
    inter_y2 = min(box1[3], box2[3])
    inter_area = max(0, inter_x2-inter_x1) * max(0, inter_y2-inter_y1)
    area1 = (box1[2]-box1[0]) * (box1[3]-box1[1])
    area2 = (box2[2]-box2[0]) * (box2[3]-box2[1])
    union_area = area1 + area2 - inter_area
    return inter_area / union_area if union_area > 0 else 0

def nms(detections: list[tuple[float, list[float]]],
        iou_threshold: float = 0.5) -> list[tuple[float, list[float]]]:
    detections = sorted(detections, key=lambda x: x[0], reverse=True)
    keep = []
    while detections:
        best = detections.pop(0)
        keep.append(best)
        detections = [(s, b) for s, b in detections
        if compute_iou(best[1], b) < iou_threshold]
    return keep