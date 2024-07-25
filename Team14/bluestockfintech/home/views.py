# from django.shortcuts import render

# def home(request):
#     return render(request, 'index.html')

# myapp/views.py

from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import matplotlib.pyplot as plt
import io

def get_status_class(status):
    if status == 1:
        return 'ongoing'
    elif status == 2:
        return 'new-listed'
    else:
        return 'coming'

def get_status_text(status):
    if status == 1:
        return 'Ongoing'
    elif status == 2:
        return 'New Listed'
    else:
        return 'Coming'

def index(request):
    page = request.GET.get('page', 1)
    records_per_page = 5

    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM ipo_info')
        total_records = cursor.fetchone()[0]

        offset = (int(page) - 1) * records_per_page
        cursor.execute('SELECT company_name, price_band, open, close, issue_size, issue_type, listing_date, status FROM ipo_info LIMIT %s OFFSET %s', [records_per_page, offset])
        records = cursor.fetchall()

    total_pages = (total_records // records_per_page) + (1 if total_records % records_per_page else 0)
    total_pages_range = range(1, total_pages + 1)

    records_with_status = [
        {
            'company_name': record[0],
            'price_band': record[1],
            'open': record[2],
            'close': record[3],
            'issue_size': record[4],
            'issue_type': record[5],
            'listing_date': record[6],
            'status': record[7],
            'status_class': get_status_class(record[7]),
            'status_text': get_status_text(record[7])
        }
        for record in records
    ]

    context = {
        'records': records_with_status,
        'page': int(page),
        'total_pages': total_pages,
        'total_pages_range': total_pages_range,
    }

    return render(request, 'upsession.html', context)

def register(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        price_band = request.POST.get('price_band')
        open_price = request.POST.get('open')
        close_price = request.POST.get('close')
        issue_size = request.POST.get('issue_size')
        issue_type = request.POST.get('issue_type')
        status = request.POST.get('status')
        ipo_price = request.POST.get('ipo_price')
        listing_price = request.POST.get('listing_price')
        listing_gain = request.POST.get('listing_gain')
        listing_date = request.POST.get('listing_date')
        cmp = request.POST.get('cmp')
        current_return = request.POST.get('current_return')
        rhp = request.POST.get('rhp')
        drhp = request.POST.get('drhp')

        # Insert data into PostgreSQL
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO ipo_info (
                        company_logo_path, company_name, price_band, open, close,
                        issue_size, issue_type, status, ipo_price, listing_price,
                        listing_gain, listing_date, cmp, current_return, rhp, drhp
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    '/static/iconss/logo.svg', company_name, price_band, open_price, close_price,
                    issue_size, issue_type, status, ipo_price, listing_price,
                    listing_gain, listing_date, cmp, current_return, rhp, drhp
                ))
            message = "Data inserted successfully!"
        except Exception as e:
            message = str(e)
        
        return render(request, 'register.html', {'message': message})

    return render(request, 'register.html', {'company_logo_path': '/static/iconss/logo.svg'})

def dashboard(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM ipo_info')
        total_ipo = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM ipo_info WHERE listing_gain::numeric > 0')
        gain_ipo = cursor.fetchone()[0]

        loss_ipo = total_ipo - gain_ipo

        cursor.execute('SELECT COUNT(*) FROM ipo_info WHERE status = 1')
        ongoing = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM ipo_info WHERE status = 2')
        new_listed = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM ipo_info WHERE status = 3')
        coming = cursor.fetchone()[0]

    context = {
        'total_ipo': total_ipo,
        'gain_ipo': gain_ipo,
        'loss_ipo': loss_ipo,
        'ongoing': ongoing,
        'new_listed': new_listed,
        'coming': coming,
    }
    
    return render(request, 'dashboard.html', context)

def chart(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT status, COUNT(*) FROM ipo_info GROUP BY status')
        rows = cursor.fetchall()

    color_map = {
        1: (199/255, 206/255, 255/255, 1),
        2: (133/255, 147/255, 237/255, 1),
        3: (90/255, 106/255, 207/255, 1)
    }

    labels = [f"Status {item[0]}" for item in rows]
    sizes = [item[1] for item in rows]
    colors = [color_map.get(item[0], (0.5, 0.5, 0.5, 1)) for item in rows]

    fig, ax = plt.subplots()

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        startangle=140,
        wedgeprops=dict(width=0.3)
    )
    ax.axis('equal')

    for text in texts + autotexts:
        text.set_fontsize(10)
        text.set_color('white')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return HttpResponse(img, content_type='image/png')