import flet
from flet import*


def main(page: Page):
    
    def rota(e):
        page.views.clear()
        page.views.append(
            View("/",
                 [ElevatedButton("pagina > ",on_click=lambda _:page.go("/2")),
                      AppBar(title=Text("home",color=colors.WHITE),bgcolor=colors.BLUE_GREY_600)],
                 bgcolor=colors.AMBER)
        )
        if page.route == "/2":
            page.views.append(
                View("/2",[ElevatedButton("volta",on_click=lambda _:page.go("/")),
                           AppBar(title=Text("p2",color=colors.WHITE),bgcolor=colors.BLACK),
                           Image(src="cave.png",width=200)],
                 bgcolor=colors.AMBER)
                )
        page.update()
        
    def views(e):
        page.views.pop()
        vv = page.views[-1]
        page.go(vv)
         
    page.on_route_change = rota
    page.on_view_pop =views  
    page.go("/")


flet.app(target=main)
