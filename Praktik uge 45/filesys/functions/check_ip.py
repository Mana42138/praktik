import asyncio
import aiohttp
import time

async def ip2(arg1):
    if arg1 == "":
        print("Invalid IP")
        return None
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://ip-api.com/json/{arg1}?fields=66846719") as r:
                if r.status == 200:
                    js = await r.json()
                    myip = ''
                    status = js.get("status")
                    if "fail" == status:
                        message = js.get("message")
                    else:
                        continent = js.get("continent", "None")
                        country = js.get("country", "None")
                        region = js.get("regionName", "None")
                        city = js.get("city", "None")
                        rue = js.get("district", "None")
                        zipcode = js.get("zip", "None")
                        lat = js.get("lat", "None")
                        lon = js.get("lon", "None")
                        timezone = js.get("timezone", "None")
                        offset = js.get("offset", "None")
                        iso = js.get("isp", "None")
                        org = js.get("org", "None")
                        reverse = js.get("reverse", "None")
                        mobile = js.get("mobile", "None")
                        proxy = js.get("proxy", "None")
                        hosting = js.get("hosting", "None")

                        log = {
                            "continent": str(continent),
                            "country": str(country),
                            "region": str(region),
                            "city": str(city),
                            "district": str(rue),
                            "zipcode": str(zipcode),
                            "latitude": str(lat),
                            "longitude": str(lon),
                            "timezone": str(timezone),
                            "offset": str(offset),
                            "isp": str(iso),
                            "organisation": str(org),
                            "reverse": str(reverse),
                            "mobile": str(mobile),
                            "proxy": str(proxy),
                            "hosting": str(hosting),
                        }
                        return log
                else:
                    print(f"Request to IP API failed for IP: {arg1}, status code: {r.status}")
                    return None
    except Exception as e:
        print(f"An error occurred while fetching data for IP: {arg1}, Error: {str(e)}")
        return None

def ip(ip3):
    return asyncio.run(ip2(ip3))