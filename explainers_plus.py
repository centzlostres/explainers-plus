"""dashAI's permutation importance and Kernel SHAP, as a plugin.

A test plugin for the dashAI plugin store: it reuses dashAI's own components
under other names. Display names end in "(plugin)" to tell them apart.
"""

from DashAI.back.core.utils import MultilingualString
from DashAI.back.explainability.explainers.kernel_shap import KernelShap
from DashAI.back.explainability.explainers.permutation_feature_importance import (
    PermutationFeatureImportance,
)


class PermutationImportancePlus(PermutationFeatureImportance):
    DISPLAY_NAME = MultilingualString(
        en="Permutation Importance Plus (plugin)",
        es="Importancia por permutación Plus (plugin)",
    )


class KernelShapPlus(KernelShap):
    DISPLAY_NAME = MultilingualString(
        en="Kernel SHAP Plus (plugin)", es="Kernel SHAP Plus (plugin)"
    )
