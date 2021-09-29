# html文件转csv文件
import pandas as pd


def main():
    name = input("Please input the name you want to save: ")
    filename = name + ".csv"
    df = []
    with open("Kusto query result for Edgeformfill.html", "r") as f:
        html = f.read()
    html_data = pd.read_html(html)
    for line in html_data:
        df.append(pd.DataFrame(line))

    result = pd.concat(df, ignore_index=True, sort=True)
    result.to_csv(filename, encoding='utf-8_sig', index=None, header=None)


if __name__ == '__main__':
    main()
