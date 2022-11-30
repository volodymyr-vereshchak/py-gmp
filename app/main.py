import asyncio
import httpx
import csv

from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

BASE_URL = "https://gmp.ent.ukrgas.com.ua/"
CONTACTED_URL = urljoin(BASE_URL, "api/devices/total-contacted")
PREFIX_URL = urljoin(BASE_URL, "api/device-reports/prefix")


@dataclass
class Connections:
    serial_number: str
    connection_number: int


async def get_total_elements(client: httpx.AsyncClient, url: str, payload: dict) -> int:
    response = await client.get(url, params=payload)
    return response.json()["totalElements"]


async def get_smart_list(client: httpx.AsyncClient, payload: dict) -> list[str]:
    response = await client.get(CONTACTED_URL, params=payload)
    return [data["serialNumber"] for data in response.json()["content"]]


def write_csv_file(
        file_name: str,
        all_content: list[Connections]
) -> None:
    with open(file_name, "w", encoding="utf-8", newline="") as csvfile:
        object_writer = csv.writer(csvfile)
        object_writer.writerow([field.name for field in fields(Connections)])
        object_writer.writerows([astuple(content) for content in all_content])


async def main():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2b2xvZHlteXIudmVyZXNoY2hhayIsImV4cCI6MTY2OTkwMzIyNCwicm9sZXMiOlsiUk9MRV9ETC1aUC1BTEwtVVNFUlMiLCJST0xFX0RMLUhPLUdNUC1NRVRST0xPR0lTVFMiLCJST0xFX0RMLUhPLUdNUC1ESVNQQVRDSEVSUyJdfQ.INTg9vfFPTAVmOLm2mtkOIS7im4rb14LXpo4romS0ovnW17JR2BNte6CFIx1-PAP6KgCD-ZbL5Inho4ggwErHQ",
    }
    
    async with httpx.AsyncClient(headers=headers) as client:
        payload = {
            "from": "20221129",
            "to": "20221130",
            "organization": 7,
            "offset": 0,
            "limit": 1,
            "filter": "manufacturerName:RGC PRODUCTION",
        }
        payload["limit"] = await get_total_elements(client, CONTACTED_URL, payload)
        smart_list = await get_smart_list(client, payload)
        connection_list = []
        single_payload = {
            "from": "20221120",
            "to": "20221130",
            "serial-number": 0,
            "manufacturer": 11,
            "channel": 0,
            "offset": 0,
            "limit": 1
        }
        for smart in smart_list:
            single_payload["serial-number"] = smart            
            connection_number = await get_total_elements(client, PREFIX_URL, single_payload)
            connection_list.append(Connections(smart, connection_number))

        write_csv_file("smart.csv", connection_list)


asyncio.run(main())
