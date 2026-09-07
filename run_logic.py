def generate_run_params(baseList, minFloor, minCeiling, minThresholdIncrement,
                        maxFloor, maxCeiling, maxThresholdIncrement,
                        normalFloor, normalCeiling, normThresholdIncrement):
    """
    Generator that yields valid run parameters based on the configuration.
    Yields: (base, minThresholdHour, minThresholdMinute, maxThresholdHour, maxThresholdMinute, normalThresholdHour, normalThresholdMinute)
    """
    for base in baseList:
        for minThresholdHour in range(minFloor, minCeiling, 2):
            for minThresholdMinute in range(0, 60, minThresholdIncrement):
                for maxThresholdHour in range(maxFloor, maxCeiling, 2):
                    for maxThresholdMinute in range(0, 60, maxThresholdIncrement):
                        for normalThresholdHour in range(normalFloor, normalCeiling):
                            for normalThresholdMinute in range(0, 60, normThresholdIncrement):
                                
                                # Logic checks
                                if minFloor <= normalFloor and minThresholdHour <= normalFloor:
                                    if minFloor <= maxFloor and minThresholdHour <= maxFloor:
                                        if normalFloor <= maxFloor and normalThresholdHour <= maxFloor:
                                            if ((normalThresholdHour < maxThresholdHour) or (
                                                    (normalThresholdHour == maxThresholdHour) and (
                                                    normalThresholdMinute <= maxThresholdMinute))):
                                                if ((minThresholdHour < normalThresholdHour) or (
                                                        (minThresholdHour == normalThresholdHour) and (
                                                        minThresholdMinute <= normalThresholdMinute))):
                                                    
                                                    yield {
                                                        "valid": True,
                                                        "base": base,
                                                        "minThresholdHour": minThresholdHour,
                                                        "minThresholdMinute": minThresholdMinute,
                                                        "maxThresholdHour": maxThresholdHour,
                                                        "maxThresholdMinute": maxThresholdMinute,
                                                        "normalThresholdHour": normalThresholdHour,
                                                        "normalThresholdMinute": normalThresholdMinute
                                                    }
                                                else:
                                                    yield {"valid": False, "reason": "min threshold > normal threshold"}
                                            else:
                                                yield {"valid": False, "reason": "normal threshold > max threshold"}
                                        else:
                                            yield {"valid": False, "reason": "normal floor > max floor"}
                                    else:
                                        yield {"valid": False, "reason": "min floor > max floor"}
                                else:
                                    yield {"valid": False, "reason": "min floor > normal floor"}
