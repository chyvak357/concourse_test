import sys
from datetime import datetime

if __name__ == "__main__":
    # print("kek")
    # print(len(sys.argv))
    # print(sys.argv)

    data = [
    "23670029        https://localhost:3000/bat/references/5a89aca7-c238-42d3-b240-a5fcd1d5f504",
    "27466356        https://localhost:3000/bat/references/cd45a2cf-426f-49f9-a6a7-5bc84f00ab12",
    "32795876        https://localhost:3000/bat/references/37cc16da-b429-47dd-b6ea-19fe35f8952e",
    "25669829        https://localhost:3000/bat/references/ea85ec4f-3adb-41f4-b7d5-b5a94b66654f",
    "34818478        https://localhost:3000/bat/references/211f41ea-99a9-4607-828c-0f9a4ff13811",
    "28283584        https://localhost:3000/bat/references/6660f2c2-9be5-4fb0-bf70-ba0e58022f29",
    "34862243        https://localhost:3000/bat/references/968d7522-8ac9-49b6-b55e-58725d87a88b",
    "11        NEW   https://localhost:3000/bat/references/a7133f80-b3b7-4675-9741-a12aa00fd6e8",
    "23559153        https://localhost:3000/bat/references/a20f2be5-43b4-4a6f-b6f2-3c0b7c16688d",
    "29401002        https://localhost:3000/bat/references/9d96e360-16f8-4889-a7d9-0c3952a004ed",
    "34527569        https://localhost:3000/bat/references/75e1b96b-52fa-49cd-8844-c55151f1d55b",
    "34475102        https://localhost:3000/bat/references/aa909922-1e8e-48d9-ab25-70d8498324f2",
    "34445211        https://localhost:3000/bat/references/1e5c8044-af8e-411f-b33b-16ecc39ddec8",
    "34637337        https://localhost:3000/bat/references/dbc23eed-38ce-46ec-97e5-7a165502ab9c",
    "28903445        https://localhost:3000/bat/references/47340f26-02ba-46b1-9ed8-3087a176bf02",
    "21690468        https://localhost:3000/bat/references/65cc2257-957f-425c-b23a-f42634bf1b89",
    "31151904        https://localhost:3000/bat/references/0e56037f-f221-43fb-8c25-6ae197fa7c35",
    "31131321        https://localhost:3000/bat/references/474d3a07-47a2-43d3-a97c-b2549ed0bc97",
    "18621636  NEW   https://localhost:3000/bat/references/b2c9ccf0-10ff-4c5f-a4c4-3c89aa76cc58",
    "19339720  NEW   https://localhost:3000/bat/references/e14c19d8-8d46-4cb9-8234-a265120c68e4",
    "28868010  NEW   https://localhost:3000/bat/references/26b109dd-05e3-45f1-98fc-0226170e5e76",
    "35328764  NEW   https://localhost:3000/bat/references/e6c22b87-bdc7-48b0-9941-559dbbab8aa9",
    "24701207  NEW   https://localhost:3000/bat/references/617e40c3-c25c-4977-b5d3-044aff9521bd",
    "32919890        https://localhost:3000/bat/references/b6718eea-87ec-4355-8af1-70b4b11d3c50",
    "34045297        https://localhost:3000/bat/references/ccefc046-56f7-4ca6-8c74-c1c33f0bdc3b",
    "28916367        https://localhost:3000/bat/references/927514db-01d5-4dd0-b391-33144f937c5a",
    ]

    body_template = """
    Hello,

    Here are the values for today:

    {}

    Best regards,
    Your Name
    """

    body = body_template.format("\n".join(data))

    with open("email-out/body", "w") as f:
        f.write(body)

    with open("email-out/subject", "w") as f:
        current_date = datetime.now().strftime("%d.%m.%Y")
        f.write(f"Obtaining AD-HOC references for {current_date}")

