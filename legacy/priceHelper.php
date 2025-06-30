<?php
function AdjustedCPC($currentCpc, $targetRoas) {
    if ($targetRoas <= 0 || $currentCpc <= 0) {
        return 0.0;
    }
    return round($currentCpc * ($targetRoas / 100), 4);
}
?>