from ddgs import DDGS

with DDGS() as ddgs:
    results = list(
        ddgs.text("Latest IPL news", max_results=5)
    )

    for result in results:
        print(result)