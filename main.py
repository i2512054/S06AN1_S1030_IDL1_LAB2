from fastapi import FastAPI
from controllers.credit_controller import router as credit_router

app = FastAPI(
    title="API de Evaluación Crediticia de Cliente de Soporte SOA",
    description="Microservicio de evaluación crediticia de cliente que usa IA para evaluar prestamo",
    version="1.0.0"
)

app.include_router(credit_router)

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "Servicio de evaluación crediticia de cliente en actividad."}
