from pydantic import BaseModel, Field
from typing import Optional

class CreditRequestInput(BaseModel):
    user_story: str = Field(..., description="Historia de usuario en lenguaje natural describiendo la solicitud de crédito.")

class CreditEvaluationDTO(BaseModel):
    requested_amount: float = Field(..., description="Monto monetario solicitado por el cliente.")
    monthly_income: float = Field(..., description="Ingresos mensuales declarados.")
    credit_history_score: str = Field(..., description="Historial crediticio estimado o reportado (Ej: Excelente, Bueno Regular, Malo).")
    risk_level: str = Field(..., description="Nivel de riesgo evaluado preliminarmente (Bajo, Medio, Alto).")
    autonomous_recommendation: str = Field(..., description="Dictamen preliminar autónomo generado por el servicio inteligente.")
    justification: str = Field(..., description="Justificación técnica basada en los parámetros extraídos.")