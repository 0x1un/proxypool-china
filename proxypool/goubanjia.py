from requests_html import HTMLSession, Element


class Goubanjia:
    def __init__(self):
        self.session = HTMLSession()
        #building request
        self.r = self.session.get(url='http://www.goubanjia.com/')
        #Find proxy ip area and choose the first one
        self.tbody = self.r.html.find("tbody")[0]
        #Find proxy ip area and find tr table
        self.trs = self.tbody.find('tr')
        #confusion decryption, A -> 0, B -> 1, Z -> 9, and the like it
        self.val = 'ABCDEFGHIZ'
        #init ip storage list
        self.ip_list = []

    def f(self, el: list) -> bool:
        '''
        The function any() returns true only if it finds any() valid value, 
        any() is only receive iterable
        '''
        return not any(el.find("[style='display: none;']")) and not any(el.find("[style='display:none;']"))
    #building parse port function
    def parse_port(self, port_element: str) -> int:
        port_list = []
        #Looping encrypted port strings to find secrets index
        for letter in port_element: #example: 'GDE'
            #Add the subscript index position in the encryption string to the list
            port_list.append(str(self.val.find(letter))) # G -> 6, D -> 3, E -> 4
        #convert the list to a string
        port = "".join(port_list)
        #decrypt the resulting port secret, need to move 3 bits to the right
        return int(port) >> 0x3 #move 634 to the right 3  : 79

    def main(self):
        for tr in self.trs:
            tds = tr.find('td')
            ips = filter(self.f, tds[0].find())
            ips = list(ips)
            real_ip = ""
            for ip in ips[:-1]:
                real_ip += ip.text.replace("\n", "")
            port_class = ips[-1].attrs.get('class')[1]
            real_port = str(self.parse_port(port_class))
            real_ip += real_port
            #yield f"{tds[2].text}://{real_ip}"
            yield f'{real_ip}'

if __name__ == '__main__':
    g = Goubanjia()
    for i in g.main():
        print(i)
