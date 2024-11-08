from graphviz import Digraph

# Create a directed graph
diagram = Digraph('Microservices to MySQL', format='png')

# Set graph attributes
diagram.attr(rankdir='LR', size='8')

# Add MySQL node
diagram.node('MySQL', shape='cylinder', style='filled', color='lightblue', label='MySQL Database')

# Add Microservice nodes
diagram.node('Service1', shape='box', style='filled', color='lightgreen', label='Microservice 1')
diagram.node('Service2', shape='box', style='filled', color='lightgreen', label='Microservice 2')
diagram.node('Service3', shape='box', style='filled', color='lightgreen', label='Microservice 3')

# Connect Microservices to MySQL Database
diagram.edge('Service1', 'MySQL', label='Connection')
diagram.edge('Service2', 'MySQL', label='Connection')
diagram.edge('Service3', 'MySQL', label='Connection')

# Render the diagram
diagram.render('microservices_to_mysql_diagram')

print("Diagram generated: microservices_to_mysql_diagram.png")

