# Phase 3
import pandas as pd

# Creates new df filtering rows by gender
def gender_segmentation(df: pd.DataFrame, genders: list = ["masculino", "femenino", "otro"]) -> pd.DataFrame:
    try:
        """
        Creates new df filtering rows by gender/s
        """
        gender_segmented_df = df.copy()
        
        normalized_genders = [gen.strip().lower() for gen in genders]
        
        # Filtering
        gender_segmented_df = gender_segmented_df[
            gender_segmented_df["genero"].astype(str).str.strip().str.lower()
            .isin(normalized_genders)
        ]

        return gender_segmented_df
    except:
        raise RuntimeError("Error al segmentar por género")


def age_segmentation(df: pd.DataFrame, segments: list) -> pd.DataFrame:
    """
    Creates new df filtering rows by age range/s
    """
    try:
        age_segmented_df = df.copy()

        # Filtering
        age_segmented_df = age_segmented_df[
            age_segmented_df["edad"].astype(str).str.strip()
            .isin(segments)
        ]

        return age_segmented_df
    except:
        raise RuntimeError("Error al segmentar por edad")
