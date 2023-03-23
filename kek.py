import sys

if __name__ == "__main__":
    # print("kek")
    # print(len(sys.argv))
    # print(sys.argv)

    data = [
        {"pmid": "23670029", "ref_no": "5a89aca7-c238-42d3-b240-a5fcd1d5f504"},
        {"pmid": "27466356", "ref_no": "cd45a2cf-426f-49f9-a6a7-5bc84f00ab12"},
        {"pmid": "36117191", "ref_no": "4b0200a8-3dcc-4251-984d-9731381d3c85"},
        {"pmid": "32641004", "ref_no": "37b3ec9b-fe66-4c2f-9600-4af6b9939c1a"},
        {"pmid": "33203665", "ref_no": "9b83440d-9ba8-40e4-8434-34537a3bdcc3"},
        {"pmid": "32795876", "ref_no": "37cc16da-b429-47dd-b6ea-19fe35f8952e"},
        {"pmid": "31604903", "ref_no": "21b16e72-fc82-4856-bef9-8f6b84a1a854"},
        {"pmid": "25669829", "ref_no": "ea85ec4f-3adb-41f4-b7d5-b5a94b66654f"},
        {"pmid": "35304405", "ref_no": "1e3fa9d9-0cc1-4c9b-b6a2-77c123013620"},
        {"pmid": "34818478", "ref_no": "211f41ea-99a9-4607-828c-0f9a4ff13811"},
        {"pmid": "31258479", "ref_no": "77dfe9c8-e6d7-49ad-ada6-1ac77a88ceb9"},
        {"pmid": "32238575", "ref_no": "e12f28b3-4965-461d-a0d0-89e306f83b76"},
        {"pmid": "28283584", "ref_no": "6660f2c2-9be5-4fb0-bf70-ba0e58022f29"},
    ]

    body_template = """
    Hello,

    Here are the values for today:

    {}

    Best regards,
    Your Name
    """

    body = body_template.format("\n".join(data))

    with open("message.txt", "w") as f:
        f.write(body)
