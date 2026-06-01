import json

class JsonRepository:

    @staticmethod
    def save(data, filepath):

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load(filepath):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)