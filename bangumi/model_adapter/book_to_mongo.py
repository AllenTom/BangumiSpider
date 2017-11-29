from bangumi.database.book import Book


def book_to_mongo(item):
    return Book(
        bangumi_id=item['bangumi_id'],
        name=item['name'], info=item['info'],
        detail=item['detail'],
        tag=item['tag'],
        author=item['author'],
        publish_date=item['publish_date'],
        press=item['press'],
        page=item['page'],
        ISBN=item['ISBN'],
        book_type=item['book_type'],
    )
