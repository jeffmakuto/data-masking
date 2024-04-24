#!/usr/bin/env python3
""" Create a dataframe """
from load_csv import DataFrameLoader


def main() -> None:
    """
    creating the dataframe from loaded csv
    """
    csv_data = """
    ID,Name,Age,Phone,Email,Card Number
    1,Martin tapelia,33,(254) 743-376-987,marttapelia@gmail.com,1245-5698-6325-0178
    2,Bella Kafukuswi,27,(254) 734-987-097,bellakafukuswi@gmail.com,8796-0987-5432-9634
    3,Benjamin Msumari,54,(254) 789-085-321,benjamsumari@gmail.com,8906-8742-9651-1287
    4,Stano Kimoda,42,(254) 712-643-289,stanokimoda@gmail.com,7143-0245-7245-0156
    5,Collo Musambati,19,(254) 789-765-014,collomusambati@gmail.com,0145-7613-0267-3891
    """
    loader = DataFrameLoader()
    loader.load_csv(csv_data)

    output_file = "output.csv"
    loader.df.to_csv(output_file, index=False)
    print(f"Dataframe has been saved to {output_file}")


if __name__ == "__main__":
    main()
