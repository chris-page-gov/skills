FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Install system deps for Pillow, image processing, and Playwright (optional)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    ffmpeg \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    libtiff5-dev \
    libwebp-dev \
    pandoc \
    curl \
    wget \
    fonts-dejavu \
    # Playwright browser deps
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    $(apt-cache show libasound2t64 >/dev/null 2>&1 && echo libasound2t64 || echo libasound2) \
    libxshmfence1 \
    libxfixes3 \
    libxext6 \
    libegl1 \
    libpci3 \
    libwayland-server0 \
    libwayland-egl1 \
    libwayland-client0 \
    && rm -rf /var/lib/apt/lists/*

# Add a few open-source fonts that skills reference (optional minimal set)
RUN mkdir -p /usr/local/share/fonts/extra \
    && echo "(Optional) Add custom fonts here if needed." \
    && fc-cache -f -v || true

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Node & Python installed via devcontainer features (see devcontainer.json)

WORKDIR /workspace

# Create non-root user matching devcontainer defaults for better host file permission mapping
RUN useradd -m -s /bin/bash vscode \
    && chown -R vscode:vscode /workspace

USER vscode