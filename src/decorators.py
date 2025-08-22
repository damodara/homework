import functools
import logging
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """
    Декоратор для логирования начала и конца выполнения функции, а также результатов или ошибок.
    :param filename: Путь к файлу, куда записывать логи. Если None — логи выводятся в консоль.
    :return: Понять бы еще что возвращает хахаха и как это описать 😁
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # Задаём общую ссылку на Handler, чтобы могли использовать как FileHandler, так и StreamHandler
                handler: logging.Handler
                if filename is not None:
                    handler = logging.FileHandler(filename)
                else:
                    handler = logging.StreamHandler(sys.stdout)

                formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
                handler.setFormatter(formatter)
                logger = logging.getLogger(func.__name__)
                logger.addHandler(handler)
                logger.setLevel(logging.INFO)

                logger.info(f"Starting execution of {func.__name__}")

                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} completed successfully with result: {result}")
            except Exception as e:
                logger.error(
                    f"{func.__name__} failed with error '{type(e).__name__}: {str(e)}'. Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()

            return result

        return wrapper

    return decorator
