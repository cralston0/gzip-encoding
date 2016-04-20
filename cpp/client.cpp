#include <iostream>
#include <fstream>

#include <json.hpp>
#include <cpr/cpr.h>

#include "GZipCodec/GZipCodec.h"

using json = nlohmann::json;

static const std::string base_url = "http://127.0.0.1:9000/";
// static const std::string base_url = "http://127.0.0.1:9000/alt/";
// static const std::string base_url = "http://127.0.0.1:9000/drf/";

void upload_plain_json(std::string data_string)
{
    auto response = cpr::Post(cpr::Url{base_url},
                              cpr::Body{data_string},
                              cpr::Header{{"Content-Type", "application/json"}});

    std::cout << "Response to plain upload:" << std::endl << response.text << std::endl;
    std::cout << "Status code was: " << response.status_code << std::endl;
}

void upload_gzip_json(std::string data_string)
{
    std::string compressedData;

    GZipCodec::Compress(data_string, compressedData);

    auto response = cpr::Post(cpr::Url{base_url},
                              cpr::Body{compressedData},
                              cpr::Header{{"Content-Type", "application/json"},
                                          {"Content-Encoding", "gzip"}});

    std::cout << "Response to gzip upload:" << std::endl << response.text << std::endl;
    std::cout << "Status code was: " << response.status_code << std::endl;
}

int main(int argc, char* argv[])
{
    json json_data;

    json_data = {
        // from https://en.wikipedia.org/wiki/JSON
        {"firstName",  "John"},
        {"lastName", "Smith"},
        {"isAlive", true,},
        {"age", 25},
        {"address", {
            {"streetAddress", "21 2nd Street"},
            {"city", "New York"},
            {"state", "NY"},
            {"postalCode", "10021-3100"}
        }},
        {"phoneNumbers", {
            {
                {"type", "home"},
                {"number", "212 555-1234"}
            },
            {
                {"type", "office"},
                {"number", "646 555-4567"}
            },
            {
                {"type", "mobile"},
                {"number", "123 456-7890"}
            }
        }},
        {"children", json::array()},
        {"spouse", NULL},
    };

    upload_plain_json(json_data.dump());
    upload_gzip_json(json_data.dump());

    return 0;
}
