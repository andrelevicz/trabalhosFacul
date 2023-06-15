import requests

response = requests.get('http://seu_servidor/items')
items = response.json()

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Tabela de Itens da Mercearia</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        img {
            max-width: 100px;
            max-height: 100px;
        }
    </style>
</head>
<body>
    <h1>Tabela de Itens da Mercearia</h1>

    <table>
        <tr>
            <th>Item</th>
            <th>Imagem</th>
            <th>Valor</th>
            <th>Descrição</th>
        </tr>
'''

for item in items:
    html += f'''
        <tr>
            <td>{item['item']}</td>
            <td><img src="{item['image']}" alt="{item['item']}"></td>
            <td>{item['value']}</td>
            <td>{item['description']}</td>
        </tr>
    '''

html += '''
    </table>
</body>
</html>
'''

print(html)