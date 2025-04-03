from litestar.config.cors import CORSConfig
from litestar.config.compression import CompressionConfig
from litestar.middleware.rate_limit import RateLimitConfig

from typing import Literal, Tuple

cors_config = CORSConfig(allow_origins=['*'])

compression_config = CompressionConfig(backend='gzip', gzip_compress_level=9)

rate_limit: Tuple[Literal['second'], int] = ('second', 100)
rate_limit_config = RateLimitConfig(rate_limit=rate_limit)
