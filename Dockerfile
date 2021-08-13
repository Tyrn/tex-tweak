FROM python:3.9.6-slim AS base

ARG user=tweaker project=tex-tweak src=tex_tweak

# Non-root user.
RUN useradd -ms /bin/bash "$user"
USER $user
WORKDIR /home/$user
ENV PATH=/home/$user/.local/bin:$PATH

# Source and project files.
RUN mkdir /home/$user/$project
WORKDIR /home/$user/$project
COPY $src ./$src/
COPY pyproject.toml ./

# Build.
RUN pip install poetry --user && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    poetry build -f sdist

FROM python:3.9.6-slim

ARG user=tweaker project=tex-tweak

# Non-root user.
RUN useradd -ms /bin/bash "$user"
USER $user
WORKDIR /home/$user
ENV PATH=/home/$user/.local/bin:$PATH

COPY --from=base /home/$user/$project/dist/ ./dist/
RUN pip install ./dist/* --user

CMD ["bash"]
