from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import User
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.programming.language import Nodejs

graph_attr = {
  "fontsize": "45",
  "bgcolor": "white",
  # "bgcolor": "transparent",
  "pad": "0.5",
}

with Diagram(show=False, graph_attr=graph_attr, filename="Remote_for_Slides"):
  user = User("User")
  users = Users("Users")

  with Cluster("NodeJS Server"):
    nodejs = Nodejs("nodejs")
    server = Server("server")
    nodejs >> server

  server >> users
  users >> Edge(color="skyblue") >> server

  user >> Edge(label="socket", color="skyblue") << server