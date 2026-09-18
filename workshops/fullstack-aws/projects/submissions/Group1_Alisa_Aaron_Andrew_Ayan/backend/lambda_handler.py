from mangum import Mangum

from backend.app.main import app

handler = Mangum(app, api_gateway_base_path="/default")
