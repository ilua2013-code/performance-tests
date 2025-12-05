from seeds.schema.result import SeedsResult
import os



def save_seeds_result(result: SeedsResult, scenario: str):
    """Сохраняет результат Seeds в JSON файл"""
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    with open(f"./dumps/{scenario}.seeds.json", "w", encoding="utf-8") as file:
        file.write(result.model_dump_json(indent=2))


def load_seeds_result(scenario: str) -> SeedsResult:
    """Загружает результат Seeds из JSON файла"""
    with open(f"./dumps/{scenario}.seeds.json", "r", encoding="utf-8") as file:
        return SeedsResult.model_validate_json(file.read())
    