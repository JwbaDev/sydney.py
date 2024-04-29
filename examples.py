import os, asyncio
from sydney import SydneyClient
from dotenv import load_dotenv
load_dotenv()

# BING_COOKIES = os.getenv("BING_COOKIES")



async def main() -> None:
    async with SydneyClient(style="creative") as sydney:
        response = await sydney.ask("Stwórz to-do app w python + flet")
        print(response)
        print()
        print('-------------------')
        print()
    async with SydneyClient(style="balanced") as sydney:
        response = await sydney.ask("Stwórz to-do app w python + flet")
        print(response)
        print()
        print('-------------------')
        print()
    async with SydneyClient(style="precise") as sydney:
        response = await sydney.ask("Stwórz to-do app w python + flet")
        print(response)
        print()
        print('-------------------')
        print()        
        

    # reset conversation
    # async with SydneyClient() as sydney:
    #     # Conversation
    #     await sydney.reset_conversation(style="creative")

    # # ask + cititations
    # async with SydneyClient() as sydney:
    #     response = await sydney.ask("When was Bing Chat released?", citations=True)
    #     print(response)


    # async with SydneyClient() as sydney:
    #     async for response in sydney.ask_stream("When was Bing Chat released?", citations=True):
    #         print(response, end="", flush=True)    
        
    # # attachment    
    # async with SydneyClient() as sydney:
    #     response = await sydney.ask("What does this picture show?", attachment="<image-url-or-path>")
    #     print(response)

    # # web context
    # async with SydneyClient() as sydney:
    #     response = await sydney.ask("Describe the webpage", context="<web-page-source>")
    #     print(response)
    
    # # search in web 
    # async with SydneyClient() as sydney:
    #     response = await sydney.ask("When was Bing Chat released?", search=False)
    #     print(response)

    # # compose 
    # async with SydneyClient() as sydney:
    #     response = await sydney.compose("Why Python is a great language", format="ideas")
    #     print(response)

    # async with SydneyClient() as sydney:
    #     async for response in sydney.compose_stream("Why Python is a great language", format="ideas"):
    #             print(response, end="", flush=True)

    # suggestions
    # async with SydneyClient() as sydney:
    #     response, suggested_responses = await sydney.ask("When was Bing Chat released?", suggestions=True)
    #     if suggested_responses:
    #         print("Suggestions:")
    #         for suggestion in suggested_responses:
    #             print(suggestion)

    # async with SydneyClient() as sydney:
    #     response, suggested_responses = await sydney.compose(
    #         "Why Python is a great language", format="ideas", suggestions=True
    #     )
    #     if suggested_responses:
    #         print("Suggestions:")
    #         for suggestion in suggested_responses:
    #             print(suggestion)
                                    
if __name__ == "__main__":
    asyncio.run(main())