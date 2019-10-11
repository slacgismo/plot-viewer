from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from .models import plot


def index(request):
    sort_options = ['location', 'season', 'mix_type']
    for options in sort_options:
        filter_value = plot.objects.order_by(options).filter().values(options).distinct()
        filtered_value = []
        for objects in filter_value:
            filtered_value.append(objects.get(options))
        filtered_value.sort()
        if options == sort_options[0]:
            distinct_locations = filtered_value.copy()
        elif options == sort_options[1]:
            distinct_seasons = filtered_value.copy()
        elif options == sort_options[2]:
            distinct_mix_types = filtered_value.copy()
    return render(request, 'base.html', {'dist_loc':distinct_locations, 'dist_season':distinct_seasons, 'dist_mt':distinct_mix_types})



class modelListView(generic.ListView):
    model = plot
    template_name = 'home.html'

    def get(self, request):
        filter_type = self.request.GET.get("filter_type")
        x_axis_input = self.request.GET.get("x_axis_search")
        y_axis_input = self.request.GET.get("y_axis_search")
        normalization_input = self.request.GET.get("normalization")
        xy_sort = []
        objects_list = []
        if (x_axis_input != None) and (y_axis_input != None) and (normalization_input != None):

            # filter is being applied for the unselected feature
            if (x_axis_input != "season") and (y_axis_input != "season"):
                objects_list1 = plot.objects.filter(season = filter_type).order_by(y_axis_input)

            elif (x_axis_input != "mix_type") and (y_axis_input != "mix_type"):
                objects_list1 = plot.objects.filter(mix_type = filter_type).order_by(y_axis_input)

            elif (x_axis_input != "location") and (y_axis_input != "location"):
                objects_list1 = plot.objects.filter(location = filter_type).order_by(y_axis_input)

            if (x_axis_input != y_axis_input):
                for object in objects_list1:
                    if getattr(object,'normalization') == normalization_input:
                        objects_list.append(object)

                # splitting all objects in to lists corresponding to y_axis_input upon sorting x_axis_input
                unique_rows = [objects_list[0]]
                for i in range(len(objects_list)-1):
                    if (getattr(objects_list[i],y_axis_input) == getattr(objects_list[i+1],y_axis_input)):
                        unique_rows.append(objects_list[i+1])
                    else:
                        xy_sort.append(unique_rows)
                        unique_rows = [objects_list[i+1]]
                xy_sort.append(unique_rows)

                # sorting the inner lists according to x_axis_input
                for x in range(len(xy_sort)):
                    xy_sort[x].sort(key=lambda x: getattr(x,x_axis_input), reverse=False)

                # to pass the distinct values into home.html
                sort_options = ['location', 'season', 'mix_type']
                for options in sort_options:
                    filter_value = plot.objects.order_by(options).filter().values(options).distinct()
                    filtered_value = []
                    for objects in filter_value:
                        filtered_value.append(objects.get(options))
                    filtered_value.sort()
                    if options == sort_options[0]:
                        distinct_locations = filtered_value.copy()
                    elif options == sort_options[1]:
                        distinct_seasons = filtered_value.copy()
                    elif options == sort_options[2]:
                        distinct_mix_types = filtered_value.copy()

                return render(request, self.template_name, {'xy_sort':xy_sort, 'x_axis_input':x_axis_input, 'y_axis_input':y_axis_input, 'filter_value':filter_type, 'normalization_input':normalization_input, 'dist_loc':distinct_locations, 'dist_season':distinct_seasons, 'dist_mt':distinct_mix_types})
            return redirect("/")
        return redirect("/")
