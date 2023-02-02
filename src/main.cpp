#include <iostream>
#include <argh.h>
#include <websocketpp/client.hpp>

#include <boost/beast.hpp>
#include <boost/beast/ssl.hpp>
#include <boost/asio.hpp>
#include <boost/asio/ssl.hpp>

namespace net = boost::asio;
namespace beast = boost::beast;
using namespace boost::beast;
using namespace boost::beast::websocket;

int main(int argc, char* argv[]) {

    argh::parser cmdl(argv);

    if (cmdl[{ "-v", "--verbose" }])

        std::cout << "Verbose, I am.\n";

    std::cout << "Hello C++" << std::endl;

    net::io_context ioc;

    tcp_stream sock(ioc);

    net::ssl::context ctx(net::ssl::context::tlsv12);

}

