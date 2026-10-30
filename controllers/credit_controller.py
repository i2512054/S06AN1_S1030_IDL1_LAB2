from fastapi import APIRouter, HTTPException, status
from models.credit_dto import CreditRequestInput, CreditEvaluationDTO
from services.llm_service import CreditLLMService

router = APIRouter(prefix="/api/v1/credits", tags=["Credit Evaluation"])
llm_service = CreditLLMService()

@router.post(
    "/evaluation",
    response_model=CreditEvaluationDTO,
    status_code=status.HTTP_200_OK,
    summary="Evaluación crediticia de un cliente mediante el uso de la Inteligencia Artificial"
)
async def evaluation_credit_endpoint(request: CreditRequestInput):
    if not request.user_story.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La historia de usuario crediticia requerida no puede estan en vacío."
        )
    
    result = llm_service.evaluate_credit_request(request)
    return result
