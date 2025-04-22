# Hard: Build a small CLI tool or Django command where each class follows SRP. Think logging, processing, saving.
# Bad SRP
def IS3_CO_Service(request, id):
    # Aggregate all required fields in one query
    service_sums = CO_Service.objects.aggregate(
        BKB_Service=Sum('BKB_Service', default=0),
        Monitoring=Sum('Monitoring', default=0),
        WiFi_Service=Sum('WiFi_Service', default=0),
        Client_Service=Sum('ISP_Service', default=0)
    )

    # Extract values with default fallback
    BKB_Service = service_sums.get('BKB_Service', 0)
    Monitoring = service_sums.get('Monitoring', 0)
    WiFi_Service = service_sums.get('WiFi_Service', 0)
    Client_Service = service_sums.get('Client_Service', 0)

    # Calculate total service count
    All_Service = BKB_Service + Monitoring + WiFi_Service + Client_Service

    # Get total bandwidth
    Total_BW = (IS3_Interface.objects.filter(Service_Type='ISP_Service').aggregate(total_bw=Sum('Config_BW', default=0)).get('total_bw', 0))
    Total_BW = round(Total_BW / 1024, 2) if Total_BW else 0

    # Fetch CO List based on the provided id
    CO_List = CO_Service.objects.all() if id == 'All_IS3' else CO_Service.objects.filter(CO_Name=id)

    # Render template with context data
    return render(request, 'IS3_Service.html', {'CO_List': CO_List,'BKB_Service': BKB_Service, 'Monitoring': Monitoring,
            'CO_Name': id, 'WiFi_Service': WiFi_Service, 'Client_Service': Client_Service, 'Total_BW': Total_BW,'All_Service': All_Service,})

# Good SRP
def calculate_total_service(request, id):
    # Aggregate all required fields in one query
    service_sums = CO_Service.objects.aggregate(
        BKB_Service=Sum('BKB_Service', default=0),
        Monitoring=Sum('Monitoring', default=0),
        WiFi_Service=Sum('WiFi_Service', default=0),
        Client_Service=Sum('ISP_Service', default=0)
    )

    return {
        'BKB_Service': service_sums.get('BKB_Service', 0),
        'Monitoring': service_sums.get('Monitoring', 0),
        'WiFi_Service': service_sums.get('WiFi_Service', 0),
        'Client_Service': service_sums.get('Client_Service', 0)
    }

def calculate_total_bw():
    total_bw = (IS3_Interface.objects.filter(Service_Type='ISP_Service').aggregate(total_bw=Sum('Config_BW', default=0)).get('total_bw', 0)).get('total_bw', 0)
    return round(total_bw / 1024, 2) if total_bw else 0

def fetch_CO_list(co_id):
    return CO_Service.objects.all() if id == 'All_IS3' else CO_Service.objects.filter(CO_Name=id)

def render_is3_service_template(request, co_id):
    # Render template with context data
    services = calculate_total_service()
    total_bw = calculate_total_bw()
    co_list = fetch_CO_list(co_id)
    all_service = sum(services.values())

    context = {**services, 'CO_List': co_list, 'CO_Name': co_id, 'Total_BW': total_bw,'All_Service': all_service,}

    return render(request, 'IS3_Service.html', context)