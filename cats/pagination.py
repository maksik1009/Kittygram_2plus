from rest_framework import pagination
# from rest_framework.response import Response


class CatsPagination(pagination.PageNumberPagination):  # BasePagination
    page_size = 10

    # def paginate_queryset(self, queryset, request, view=None):
    #     # 1. Получаем номер страницы из параметров URL (?page=2)
    #     # Если параметра нет, считаем, что страница 1
    #     page_number = int(request.query_params.get('page', 1))

    #     # 2. Считаем границы среза
    #     start = (page_number - 1) * self.page_size
    #     end = start + self.page_size

    #     # 3. Сохраняем данные для ссылок (они понадобятся в get_paginated_response)
    #     self.request = request
    #     self.count = queryset.count() # Общее количество объектов
    #     self.page_number = page_number

    #     # 4. Возвращаем нарезанный список
    #     return list(queryset[start:end])

    # def get_paginated_response(self, data):
    #     # Тут ты используешь данные, которые сохранил выше
    #     return Response({
    #         'Вперед': self.get_next_link(),
    #         'Назад': self.get_previous_link(),
    #         'Количество': self.count,
    #         'Результат': data
    #     })

    # def get_next_link(self):
    #     # Логика генерации ссылки на следующую страницу
    #     if self.page_number * self.page_size >= self.count:
    #         return None
    #     url = self.request.build_absolute_uri()
    #     # Это упрощенно, в реальном DRF логика замены цифры в URL сложнее
    #     return f"Тут будет ссылка на страницу {self.page_number + 1}"

    # def get_previous_link(self):
    #     if self.page_number <= 1:
    #         return None
    #     return f"Тут будет ссылка на страницу {self.page_number - 1}"
