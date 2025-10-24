# API接口文档

共发现 551 个API端点

## 模块: /

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `https://github.com/infiniflow/ragflow` |  | web\src\constants\agent.ts |

## 模块: /<canvas_id>

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/<canvas_id>/sessions` |  | api\apps\canvas_app.py |
| GET | `/<canvas_id>/sessions` |  | api\apps\canvas_app.py |

## 模块: /<kb_id>

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/<kb_id>/tags` |  | api\apps\kb_app.py |
| POST | `/<kb_id>/rm_tags` |  | api\apps\kb_app.py |
| POST | `/<kb_id>/rename_tag` |  | api\apps\kb_app.py |
| GET | `/<kb_id>/knowledge_graph` |  | api\apps\kb_app.py |
| DELETE | `/<kb_id>/knowledge_graph` |  | api\apps\kb_app.py |
| GET | `/<kb_id>/tags` |  | api\apps\kb_app.py |
| POST | `/<kb_id>/rm_tags` |  | api\apps\kb_app.py |
| POST | `/<kb_id>/rename_tag` |  | api\apps\kb_app.py |
| GET | `/<kb_id>/knowledge_graph` |  | api\apps\kb_app.py |
| DELETE | `/<kb_id>/knowledge_graph` |  | api\apps\kb_app.py |

## 模块: /<tenant_id>

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/<tenant_id>/user/list` |  | api\apps\tenant_app.py |
| POST | `/<tenant_id>/user` |  | api\apps\tenant_app.py |
| DELETE | `/<tenant_id>/user/<user_id>` |  | api\apps\tenant_app.py |
| GET | `/<tenant_id>/user/list` |  | api\apps\tenant_app.py |
| POST | `/<tenant_id>/user` |  | api\apps\tenant_app.py |
| DELETE | `/<tenant_id>/user/<user_id>` |  | api\apps\tenant_app.py |

## 模块: /add_llm

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/add_llm` |  | api\apps\llm_app.py |
| POST | `/add_llm` |  | api\apps\llm_app.py |

## 模块: /agentbots

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/agentbots/<agent_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/agentbots/<agent_id>/inputs` |  | api\apps\sdk\session.py |
| POST | `/agentbots/<agent_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/agentbots/<agent_id>/inputs` |  | api\apps\sdk\session.py |

## 模块: /agents

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/agents` |  | api\apps\sdk\agent.py |
| POST | `/agents` |  | api\apps\sdk\agent.py |
| PUT | `/agents/<agent_id>` |  | api\apps\sdk\agent.py |
| DELETE | `/agents/<agent_id>` |  | api\apps\sdk\agent.py |
| GET | `/agents` |  | api\apps\sdk\agent.py |
| POST | `/agents` |  | api\apps\sdk\agent.py |
| PUT | `/agents/<agent_id>` |  | api\apps\sdk\agent.py |
| DELETE | `/agents/<agent_id>` |  | api\apps\sdk\agent.py |
| POST | `/agents/<agent_id>/sessions` |  | api\apps\sdk\session.py |
| POST | `/agents/<agent_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/agents/<agent_id>/sessions` |  | api\apps\sdk\session.py |
| DELETE | `/agents/<agent_id>/sessions` |  | api\apps\sdk\session.py |
| POST | `/agents/<agent_id>/sessions` |  | api\apps\sdk\session.py |
| POST | `/agents/<agent_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/agents/<agent_id>/sessions` |  | api\apps\sdk\session.py |
| DELETE | `/agents/<agent_id>/sessions` |  | api\apps\sdk\session.py |

## 模块: /agents_openai

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/agents_openai/<agent_id>/chat/completions` |  | api\apps\sdk\session.py |
| POST | `/agents_openai/<agent_id>/chat/completions` |  | api\apps\sdk\session.py |

## 模块: /agree

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| PUT | `/agree/<tenant_id>` |  | api\apps\tenant_app.py |
| PUT | `/agree/<tenant_id>` |  | api\apps\tenant_app.py |

## 模块: /all_parent_folder

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/all_parent_folder` |  | api\apps\file_app.py |
| GET | `/all_parent_folder` |  | api\apps\file_app.py |

## 模块: /api_key

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/api_key` |  | api\apps\langfuse_app.py |
| PUT | `/api_key` |  | api\apps\langfuse_app.py |
| GET | `/api_key` |  | api\apps\langfuse_app.py |
| DELETE | `/api_key` |  | api\apps\langfuse_app.py |
| POST | `/api_key` |  | api\apps\langfuse_app.py |
| PUT | `/api_key` |  | api\apps\langfuse_app.py |
| GET | `/api_key` |  | api\apps\langfuse_app.py |
| DELETE | `/api_key` |  | api\apps\langfuse_app.py |

## 模块: /ask

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/ask` |  | api\apps\conversation_app.py |
| POST | `/ask` |  | api\apps\conversation_app.py |

## 模块: /auth

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/auth` |  | admin\server\routes.py |
| GET | `/auth` |  | admin\server\routes.py |

## 模块: /basic_info

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/basic_info` |  | api\apps\kb_app.py |
| GET | `/basic_info` |  | api\apps\kb_app.py |

## 模块: /cache_tools

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/cache_tools` |  | api\apps\mcp_server_app.py |
| POST | `/cache_tools` |  | api\apps\mcp_server_app.py |

## 模块: /cancel

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| PUT | `/cancel/<task_id>` |  | api\apps\canvas_app.py |
| PUT | `/cancel/<task_id>` |  | api\apps\canvas_app.py |

## 模块: /change_parser

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/change_parser` |  | api\apps\document_app.py |
| POST | `/change_parser` |  | api\apps\document_app.py |

## 模块: /change_status

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/change_status` |  | api\apps\document_app.py |
| POST | `/change_status` |  | api\apps\document_app.py |

## 模块: /chatbots

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/chatbots/<dialog_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/chatbots/<dialog_id>/info` |  | api\apps\sdk\session.py |
| POST | `/chatbots/<dialog_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/chatbots/<dialog_id>/info` |  | api\apps\sdk\session.py |

## 模块: /chats

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/chats` |  | api\apps\sdk\chat.py |
| PUT | `/chats/<chat_id>` |  | api\apps\sdk\chat.py |
| DELETE | `/chats` |  | api\apps\sdk\chat.py |
| GET | `/chats` |  | api\apps\sdk\chat.py |
| POST | `/chats` |  | api\apps\sdk\chat.py |
| PUT | `/chats/<chat_id>` |  | api\apps\sdk\chat.py |
| DELETE | `/chats` |  | api\apps\sdk\chat.py |
| GET | `/chats` |  | api\apps\sdk\chat.py |
| POST | `/chats/<chat_id>/sessions` |  | api\apps\sdk\session.py |
| PUT | `/chats/<chat_id>/sessions/<session_id>` |  | api\apps\sdk\session.py |
| POST | `/chats/<chat_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/chats/<chat_id>/sessions` |  | api\apps\sdk\session.py |
| DELETE | `/chats/<chat_id>/sessions` |  | api\apps\sdk\session.py |
| POST | `/chats/<chat_id>/sessions` |  | api\apps\sdk\session.py |
| PUT | `/chats/<chat_id>/sessions/<session_id>` |  | api\apps\sdk\session.py |
| POST | `/chats/<chat_id>/completions` |  | api\apps\sdk\session.py |
| GET | `/chats/<chat_id>/sessions` |  | api\apps\sdk\session.py |
| DELETE | `/chats/<chat_id>/sessions` |  | api\apps\sdk\session.py |

## 模块: /chats_openai

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/chats_openai/<chat_id>/chat/completions` |  | api\apps\sdk\session.py |
| POST | `/chats_openai/<chat_id>/chat/completions` |  | api\apps\sdk\session.py |

## 模块: /completion

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/completion` |  | api\apps\api_app.py |
| POST | `/completion` |  | api\apps\api_app.py |
| POST | `/completion` |  | api\apps\canvas_app.py |
| POST | `/completion` |  | api\apps\canvas_app.py |
| POST | `/completion` |  | api\apps\conversation_app.py |
| POST | `/completion` |  | api\apps\conversation_app.py |

## 模块: /completion_aibotk

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/completion_aibotk` |  | api\apps\api_app.py |
| POST | `/completion_aibotk` |  | api\apps\api_app.py |

## 模块: /conf.json

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/conf.json` |  | web\src\hooks\logic-hooks.ts |

## 模块: /config

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/config` |  | api\apps\system_app.py |
| GET | `/config` |  | api\apps\system_app.py |

## 模块: /conversation

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/conversation/<conversation_id>` |  | api\apps\api_app.py |
| GET | `/conversation/<conversation_id>` |  | api\apps\api_app.py |

## 模块: /convert

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/convert` |  | api\apps\file2document_app.py |
| POST | `/convert` |  | api\apps\file2document_app.py |

## 模块: /create

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/create` |  | api\apps\chunk_app.py |
| POST | `/create` |  | api\apps\chunk_app.py |
| POST | `/create` |  | api\apps\document_app.py |
| POST | `/create` |  | api\apps\document_app.py |
| POST | `/create` |  | api\apps\file_app.py |
| POST | `/create` |  | api\apps\file_app.py |
| POST | `/create` |  | api\apps\mcp_server_app.py |
| POST | `/create` |  | api\apps\mcp_server_app.py |

## 模块: /datasets

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/datasets` |  | api\apps\sdk\dataset.py |
| DELETE | `/datasets` |  | api\apps\sdk\dataset.py |
| PUT | `/datasets/<dataset_id>` |  | api\apps\sdk\dataset.py |
| GET | `/datasets` |  | api\apps\sdk\dataset.py |
| GET | `/datasets/<dataset_id>/knowledge_graph` |  | api\apps\sdk\dataset.py |
| DELETE | `/datasets/<dataset_id>/knowledge_graph` |  | api\apps\sdk\dataset.py |
| POST | `/datasets` |  | api\apps\sdk\dataset.py |
| DELETE | `/datasets` |  | api\apps\sdk\dataset.py |
| PUT | `/datasets/<dataset_id>` |  | api\apps\sdk\dataset.py |
| GET | `/datasets` |  | api\apps\sdk\dataset.py |
| GET | `/datasets/<dataset_id>/knowledge_graph` |  | api\apps\sdk\dataset.py |
| DELETE | `/datasets/<dataset_id>/knowledge_graph` |  | api\apps\sdk\dataset.py |
| POST | `/datasets/<dataset_id>/documents` |  | api\apps\sdk\doc.py |
| PUT | `/datasets/<dataset_id>/documents/<document_id>` |  | api\apps\sdk\doc.py |
| GET | `/datasets/<dataset_id>/documents/<document_id>` |  | api\apps\sdk\doc.py |
| GET | `/datasets/<dataset_id>/documents` |  | api\apps\sdk\doc.py |
| DELETE | `/datasets/<dataset_id>/documents` |  | api\apps\sdk\doc.py |
| POST | `/datasets/<dataset_id>/chunks` |  | api\apps\sdk\doc.py |
| DELETE | `/datasets/<dataset_id>/chunks` |  | api\apps\sdk\doc.py |
| GET | `/datasets/<dataset_id>/documents/<document_id>/chunks` |  | api\apps\sdk\doc.py |
| POST | `/datasets/<dataset_id>/documents` |  | api\apps\sdk\doc.py |
| PUT | `/datasets/<dataset_id>/documents/<document_id>` |  | api\apps\sdk\doc.py |
| GET | `/datasets/<dataset_id>/documents/<document_id>` |  | api\apps\sdk\doc.py |
| GET | `/datasets/<dataset_id>/documents` |  | api\apps\sdk\doc.py |
| DELETE | `/datasets/<dataset_id>/documents` |  | api\apps\sdk\doc.py |
| POST | `/datasets/<dataset_id>/chunks` |  | api\apps\sdk\doc.py |
| DELETE | `/datasets/<dataset_id>/chunks` |  | api\apps\sdk\doc.py |
| GET | `/datasets/<dataset_id>/documents/<document_id>/chunks` |  | api\apps\sdk\doc.py |

## 模块: /debug

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/debug` |  | api\apps\canvas_app.py |
| POST | `/debug` |  | api\apps\canvas_app.py |

## 模块: /delete_factory

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/delete_factory` |  | api\apps\llm_app.py |
| POST | `/delete_factory` |  | api\apps\llm_app.py |

## 模块: /delete_llm

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/delete_llm` |  | api\apps\llm_app.py |
| POST | `/delete_llm` |  | api\apps\llm_app.py |

## 模块: /delete_msg

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/delete_msg` |  | api\apps\conversation_app.py |
| POST | `/delete_msg` |  | api\apps\conversation_app.py |

## 模块: /delete_pipeline_logs

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/delete_pipeline_logs` |  | api\apps\kb_app.py |
| POST | `/delete_pipeline_logs` |  | api\apps\kb_app.py |

## 模块: /detail

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/detail` |  | api\apps\kb_app.py |
| GET | `/detail` |  | api\apps\kb_app.py |
| GET | `/detail` |  | api\apps\mcp_server_app.py |
| GET | `/detail` |  | api\apps\mcp_server_app.py |
| GET | `/detail` |  | api\apps\search_app.py |
| GET | `/detail` |  | api\apps\search_app.py |

## 模块: /dify

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/dify/retrieval` |  | api\apps\sdk\dify_retrieval.py |
| POST | `/dify/retrieval` |  | api\apps\sdk\dify_retrieval.py |

## 模块: /document

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/document/upload` |  | api\apps\api_app.py |
| POST | `/document/upload_and_parse` |  | api\apps\api_app.py |
| POST | `/document/infos` |  | api\apps\api_app.py |
| DELETE | `/document` |  | api\apps\api_app.py |
| POST | `/document/upload` |  | api\apps\api_app.py |
| POST | `/document/upload_and_parse` |  | api\apps\api_app.py |
| POST | `/document/infos` |  | api\apps\api_app.py |
| DELETE | `/document` |  | api\apps\api_app.py |

## 模块: /download

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/download` |  | api\apps\canvas_app.py |
| GET | `/download` |  | api\apps\canvas_app.py |

## 模块: /export

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/export` |  | api\apps\mcp_server_app.py |
| POST | `/export` |  | api\apps\mcp_server_app.py |

## 模块: /factories

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/factories` |  | api\apps\llm_app.py |
| GET | `/factories` |  | api\apps\llm_app.py |

## 模块: /feishu_callback

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/feishu_callback` |  | api\apps\user_app.py |
| GET | `/feishu_callback` |  | api\apps\user_app.py |

## 模块: /file

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/file/upload` |  | api\apps\sdk\files.py |
| POST | `/file/create` |  | api\apps\sdk\files.py |
| GET | `/file/list` |  | api\apps\sdk\files.py |
| GET | `/file/root_folder` |  | api\apps\sdk\files.py |
| GET | `/file/parent_folder` |  | api\apps\sdk\files.py |
| GET | `/file/all_parent_folder` |  | api\apps\sdk\files.py |
| POST | `/file/rm` |  | api\apps\sdk\files.py |
| POST | `/file/rename` |  | api\apps\sdk\files.py |
| GET | `/file/get/<file_id>` |  | api\apps\sdk\files.py |
| POST | `/file/mv` |  | api\apps\sdk\files.py |
| POST | `/file/convert` |  | api\apps\sdk\files.py |
| POST | `/file/upload` |  | api\apps\sdk\files.py |
| POST | `/file/create` |  | api\apps\sdk\files.py |
| GET | `/file/list` |  | api\apps\sdk\files.py |
| GET | `/file/root_folder` |  | api\apps\sdk\files.py |
| GET | `/file/parent_folder` |  | api\apps\sdk\files.py |
| GET | `/file/all_parent_folder` |  | api\apps\sdk\files.py |
| POST | `/file/rm` |  | api\apps\sdk\files.py |
| POST | `/file/rename` |  | api\apps\sdk\files.py |
| GET | `/file/get/<file_id>` |  | api\apps\sdk\files.py |
| POST | `/file/mv` |  | api\apps\sdk\files.py |
| POST | `/file/convert` |  | api\apps\sdk\files.py |

## 模块: /filter

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/filter` |  | api\apps\document_app.py |
| POST | `/filter` |  | api\apps\document_app.py |

## 模块: /forget

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/forget/captcha` |  | api\apps\user_app.py |
| POST | `/forget/otp` |  | api\apps\user_app.py |
| POST | `/forget` |  | api\apps\user_app.py |
| GET | `/forget/captcha` |  | api\apps\user_app.py |
| POST | `/forget/otp` |  | api\apps\user_app.py |
| POST | `/forget` |  | api\apps\user_app.py |

## 模块: /get

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/get/<canvas_id>` |  | api\apps\canvas_app.py |
| GET | `/get/<canvas_id>` |  | api\apps\canvas_app.py |
| GET | `/get` |  | api\apps\chunk_app.py |
| GET | `/get` |  | api\apps\chunk_app.py |
| GET | `/get` |  | api\apps\conversation_app.py |
| GET | `/get` |  | api\apps\conversation_app.py |
| GET | `/get` |  | api\apps\dialog_app.py |
| GET | `/get` |  | api\apps\dialog_app.py |
| GET | `/get/<doc_id>` |  | api\apps\document_app.py |
| GET | `/get/<doc_id>` |  | api\apps\document_app.py |
| GET | `/get/<file_id>` |  | api\apps\file_app.py |
| GET | `/get/<file_id>` |  | api\apps\file_app.py |

## 模块: /get_chunk

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/get_chunk/<chunk_id>` |  | api\apps\api_app.py |
| GET | `/get_chunk/<chunk_id>` |  | api\apps\api_app.py |

## 模块: /get_meta

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/get_meta` |  | api\apps\kb_app.py |
| GET | `/get_meta` |  | api\apps\kb_app.py |

## 模块: /getlistversion

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/getlistversion/<canvas_id>` |  | api\apps\canvas_app.py |
| GET | `/getlistversion/<canvas_id>` |  | api\apps\canvas_app.py |

## 模块: /getsse

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/getsse/<canvas_id>` |  | api\apps\canvas_app.py |
| GET | `/getsse/<canvas_id>` |  | api\apps\canvas_app.py |
| GET | `/getsse/<dialog_id>` |  | api\apps\conversation_app.py |
| GET | `/getsse/<dialog_id>` |  | api\apps\conversation_app.py |

## 模块: /getversion

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/getversion/<version_id>` |  | api\apps\canvas_app.py |
| GET | `/getversion/<version_id>` |  | api\apps\canvas_app.py |

## 模块: /github_callback

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/github_callback` |  | api\apps\user_app.py |
| GET | `/github_callback` |  | api\apps\user_app.py |

## 模块: /healthz

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/healthz` |  | api\apps\system_app.py |
| GET | `/healthz` |  | api\apps\system_app.py |

## 模块: /image

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/image/<image_id>` |  | api\apps\document_app.py |
| GET | `/image/<image_id>` |  | api\apps\document_app.py |

## 模块: /import

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/import` |  | api\apps\mcp_server_app.py |
| POST | `/import` |  | api\apps\mcp_server_app.py |

## 模块: /info

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/info` |  | api\apps\user_app.py |
| GET | `/info` |  | api\apps\user_app.py |

## 模块: /infos

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/infos` |  | api\apps\document_app.py |
| POST | `/infos` |  | api\apps\document_app.py |

## 模块: /input_form

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/input_form` |  | api\apps\canvas_app.py |
| GET | `/input_form` |  | api\apps\canvas_app.py |

## 模块: /knowledge_graph

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/knowledge_graph` |  | api\apps\chunk_app.py |
| GET | `/knowledge_graph` |  | api\apps\chunk_app.py |

## 模块: /list

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/list` |  | api\apps\canvas_app.py |
| GET | `/list` |  | api\apps\canvas_app.py |
| POST | `/list` |  | api\apps\chunk_app.py |
| POST | `/list` |  | api\apps\chunk_app.py |
| GET | `/list` |  | api\apps\conversation_app.py |
| GET | `/list` |  | api\apps\conversation_app.py |
| GET | `/list` |  | api\apps\dialog_app.py |
| GET | `/list` |  | api\apps\dialog_app.py |
| POST | `/list` |  | api\apps\document_app.py |
| POST | `/list` |  | api\apps\document_app.py |
| GET | `/list` |  | api\apps\file_app.py |
| GET | `/list` |  | api\apps\file_app.py |
| POST | `/list` |  | api\apps\kb_app.py |
| POST | `/list` |  | api\apps\kb_app.py |
| GET | `/list` |  | api\apps\llm_app.py |
| GET | `/list` |  | api\apps\llm_app.py |
| POST | `/list` |  | api\apps\mcp_server_app.py |
| POST | `/list` |  | api\apps\mcp_server_app.py |
| POST | `/list` |  | api\apps\search_app.py |
| POST | `/list` |  | api\apps\search_app.py |
| GET | `/list` |  | api\apps\tenant_app.py |
| GET | `/list` |  | api\apps\tenant_app.py |

## 模块: /list_chunks

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/list_chunks` |  | api\apps\api_app.py |
| POST | `/list_chunks` |  | api\apps\api_app.py |

## 模块: /list_kb_docs

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/list_kb_docs` |  | api\apps\api_app.py |
| POST | `/list_kb_docs` |  | api\apps\api_app.py |

## 模块: /list_pipeline_dataset_logs

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/list_pipeline_dataset_logs` |  | api\apps\kb_app.py |
| POST | `/list_pipeline_dataset_logs` |  | api\apps\kb_app.py |

## 模块: /list_pipeline_logs

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/list_pipeline_logs` |  | api\apps\kb_app.py |
| POST | `/list_pipeline_logs` |  | api\apps\kb_app.py |

## 模块: /list_tools

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/list_tools` |  | api\apps\mcp_server_app.py |
| POST | `/list_tools` |  | api\apps\mcp_server_app.py |

## 模块: /llm_tools

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/llm_tools` |  | api\apps\plugin_app.py |
| GET | `/llm_tools` |  | api\apps\plugin_app.py |

## 模块: /login

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/login` |  | api\apps\user_app.py |
| GET | `/login` |  | api\apps\user_app.py |
| GET | `/login/channels` |  | api\apps\user_app.py |
| GET | `/login/<channel>` |  | api\apps\user_app.py |
| POST | `/login` |  | api\apps\user_app.py |
| GET | `/login` |  | api\apps\user_app.py |
| GET | `/login/channels` |  | api\apps\user_app.py |
| GET | `/login/<channel>` |  | api\apps\user_app.py |
| POST | `/login` |  | admin\server\routes.py |
| POST | `/login` |  | admin\server\routes.py |

## 模块: /logout

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/logout` |  | api\apps\user_app.py |
| GET | `/logout` |  | api\apps\user_app.py |
| GET | `/logout` |  | admin\server\routes.py |
| GET | `/logout` |  | admin\server\routes.py |

## 模块: /mindmap

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/mindmap` |  | api\apps\conversation_app.py |
| POST | `/mindmap` |  | api\apps\conversation_app.py |

## 模块: /mv

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/mv` |  | api\apps\file_app.py |
| POST | `/mv` |  | api\apps\file_app.py |

## 模块: /my_llms

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/my_llms` |  | api\apps\llm_app.py |
| GET | `/my_llms` |  | api\apps\llm_app.py |

## 模块: /new_conversation

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/new_conversation` |  | api\apps\api_app.py |
| GET | `/new_conversation` |  | api\apps\api_app.py |

## 模块: /new_token

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/new_token` |  | api\apps\api_app.py |
| POST | `/new_token` |  | api\apps\api_app.py |
| POST | `/new_token` |  | api\apps\system_app.py |
| POST | `/new_token` |  | api\apps\system_app.py |

## 模块: /next

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/next` |  | api\apps\dialog_app.py |
| POST | `/next` |  | api\apps\dialog_app.py |

## 模块: /oauth

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/oauth/callback/<channel>` |  | api\apps\user_app.py |
| GET | `/oauth/callback/<channel>` |  | api\apps\user_app.py |

## 模块: /parent_folder

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/parent_folder` |  | api\apps\file_app.py |
| GET | `/parent_folder` |  | api\apps\file_app.py |

## 模块: /parse

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/parse` |  | api\apps\document_app.py |
| POST | `/parse` |  | api\apps\document_app.py |

## 模块: /path

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/path` |  | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |
| POST | `/path` |  | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |
| GET | `/path` |  | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |
| GET | `/path` |  | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |
| POST | `/path` |  | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |
| GET | `/path` |  | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |

## 模块: /ping

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/ping` |  | api\apps\system_app.py |
| GET | `/ping` |  | api\apps\system_app.py |

## 模块: /pipeline_log_detail

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/pipeline_log_detail` |  | api\apps\kb_app.py |
| GET | `/pipeline_log_detail` |  | api\apps\kb_app.py |

## 模块: /prompts

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/prompts` |  | api\apps\canvas_app.py |
| GET | `/prompts` |  | api\apps\canvas_app.py |

## 模块: /register

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/register` |  | api\apps\user_app.py |
| POST | `/register` |  | api\apps\user_app.py |

## 模块: /related_questions

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/related_questions` |  | api\apps\conversation_app.py |
| POST | `/related_questions` |  | api\apps\conversation_app.py |

## 模块: /rename

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/rename` |  | api\apps\document_app.py |
| POST | `/rename` |  | api\apps\document_app.py |
| POST | `/rename` |  | api\apps\file_app.py |
| POST | `/rename` |  | api\apps\file_app.py |

## 模块: /rerun

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/rerun` |  | api\apps\canvas_app.py |
| POST | `/rerun` |  | api\apps\canvas_app.py |

## 模块: /reset

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/reset` |  | api\apps\canvas_app.py |
| POST | `/reset` |  | api\apps\canvas_app.py |

## 模块: /retrieval

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/retrieval` |  | api\apps\api_app.py |
| POST | `/retrieval` |  | api\apps\api_app.py |
| POST | `/retrieval` |  | api\apps\sdk\doc.py |
| POST | `/retrieval` |  | api\apps\sdk\doc.py |

## 模块: /retrieval_test

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/retrieval_test` |  | api\apps\chunk_app.py |
| POST | `/retrieval_test` |  | api\apps\chunk_app.py |

## 模块: /rm

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/rm` |  | api\apps\api_app.py |
| POST | `/rm` |  | api\apps\api_app.py |
| POST | `/rm` |  | api\apps\canvas_app.py |
| POST | `/rm` |  | api\apps\canvas_app.py |
| POST | `/rm` |  | api\apps\chunk_app.py |
| POST | `/rm` |  | api\apps\chunk_app.py |
| POST | `/rm` |  | api\apps\conversation_app.py |
| POST | `/rm` |  | api\apps\conversation_app.py |
| POST | `/rm` |  | api\apps\dialog_app.py |
| POST | `/rm` |  | api\apps\dialog_app.py |
| POST | `/rm` |  | api\apps\document_app.py |
| POST | `/rm` |  | api\apps\document_app.py |
| POST | `/rm` |  | api\apps\file2document_app.py |
| POST | `/rm` |  | api\apps\file2document_app.py |
| POST | `/rm` |  | api\apps\file_app.py |
| POST | `/rm` |  | api\apps\file_app.py |
| POST | `/rm` |  | api\apps\mcp_server_app.py |
| POST | `/rm` |  | api\apps\mcp_server_app.py |

## 模块: /roles

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/roles` |  | admin\server\routes.py |
| PUT | `/roles/<role_name>` |  | admin\server\routes.py |
| DELETE | `/roles/<role_name>` |  | admin\server\routes.py |
| GET | `/roles` |  | admin\server\routes.py |
| GET | `/roles/<role_name>/permission` |  | admin\server\routes.py |
| POST | `/roles/<role_name>/permission` |  | admin\server\routes.py |
| DELETE | `/roles/<role_name>/permission` |  | admin\server\routes.py |
| POST | `/roles` |  | admin\server\routes.py |
| PUT | `/roles/<role_name>` |  | admin\server\routes.py |
| DELETE | `/roles/<role_name>` |  | admin\server\routes.py |
| GET | `/roles` |  | admin\server\routes.py |
| GET | `/roles/<role_name>/permission` |  | admin\server\routes.py |
| POST | `/roles/<role_name>/permission` |  | admin\server\routes.py |
| DELETE | `/roles/<role_name>/permission` |  | admin\server\routes.py |

## 模块: /root_folder

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/root_folder` |  | api\apps\file_app.py |
| GET | `/root_folder` |  | api\apps\file_app.py |

## 模块: /run

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/run` |  | api\apps\document_app.py |
| POST | `/run` |  | api\apps\document_app.py |

## 模块: /run_graphrag

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/run_graphrag` |  | api\apps\kb_app.py |
| POST | `/run_graphrag` |  | api\apps\kb_app.py |

## 模块: /run_mindmap

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/run_mindmap` |  | api\apps\kb_app.py |
| POST | `/run_mindmap` |  | api\apps\kb_app.py |

## 模块: /run_raptor

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/run_raptor` |  | api\apps\kb_app.py |
| POST | `/run_raptor` |  | api\apps\kb_app.py |

## 模块: /searchbots

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/searchbots/ask` |  | api\apps\sdk\session.py |
| POST | `/searchbots/retrieval_test` |  | api\apps\sdk\session.py |
| POST | `/searchbots/related_questions` |  | api\apps\sdk\session.py |
| GET | `/searchbots/detail` |  | api\apps\sdk\session.py |
| POST | `/searchbots/mindmap` |  | api\apps\sdk\session.py |
| POST | `/searchbots/ask` |  | api\apps\sdk\session.py |
| POST | `/searchbots/retrieval_test` |  | api\apps\sdk\session.py |
| POST | `/searchbots/related_questions` |  | api\apps\sdk\session.py |
| GET | `/searchbots/detail` |  | api\apps\sdk\session.py |
| POST | `/searchbots/mindmap` |  | api\apps\sdk\session.py |

## 模块: /service_types

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/service_types/<service_type>` |  | admin\server\routes.py |
| GET | `/service_types/<service_type>` |  | admin\server\routes.py |

## 模块: /services

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/services` |  | admin\server\routes.py |
| GET | `/services/<service_id>` |  | admin\server\routes.py |
| DELETE | `/services/<service_id>` |  | admin\server\routes.py |
| PUT | `/services/<service_id>` |  | admin\server\routes.py |
| GET | `/services` |  | admin\server\routes.py |
| GET | `/services/<service_id>` |  | admin\server\routes.py |
| DELETE | `/services/<service_id>` |  | admin\server\routes.py |
| PUT | `/services/<service_id>` |  | admin\server\routes.py |

## 模块: /sessions

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/sessions/ask` |  | api\apps\sdk\session.py |
| POST | `/sessions/related_questions` |  | api\apps\sdk\session.py |
| POST | `/sessions/ask` |  | api\apps\sdk\session.py |
| POST | `/sessions/related_questions` |  | api\apps\sdk\session.py |

## 模块: /set

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/set` |  | api\apps\canvas_app.py |
| POST | `/set` |  | api\apps\canvas_app.py |
| POST | `/set` |  | api\apps\chunk_app.py |
| POST | `/set` |  | api\apps\chunk_app.py |
| POST | `/set` |  | api\apps\conversation_app.py |
| POST | `/set` |  | api\apps\conversation_app.py |
| POST | `/set` |  | api\apps\dialog_app.py |
| POST | `/set` |  | api\apps\dialog_app.py |

## 模块: /set_api_key

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/set_api_key` |  | api\apps\llm_app.py |
| POST | `/set_api_key` |  | api\apps\llm_app.py |

## 模块: /set_meta

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/set_meta` |  | api\apps\document_app.py |
| POST | `/set_meta` |  | api\apps\document_app.py |

## 模块: /set_tenant_info

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/set_tenant_info` |  | api\apps\user_app.py |
| POST | `/set_tenant_info` |  | api\apps\user_app.py |

## 模块: /setting

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/setting` |  | api\apps\canvas_app.py |
| POST | `/setting` |  | api\apps\canvas_app.py |
| POST | `/setting` |  | api\apps\user_app.py |
| POST | `/setting` |  | api\apps\user_app.py |

## 模块: /stats

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/stats` |  | api\apps\api_app.py |
| GET | `/stats` |  | api\apps\api_app.py |

## 模块: /status

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/status` |  | api\apps\system_app.py |
| GET | `/status` |  | api\apps\system_app.py |

## 模块: /switch

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/switch` |  | api\apps\chunk_app.py |
| POST | `/switch` |  | api\apps\chunk_app.py |

## 模块: /tags

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/tags` |  | api\apps\kb_app.py |
| GET | `/tags` |  | api\apps\kb_app.py |

## 模块: /templates

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/templates` |  | api\apps\canvas_app.py |
| GET | `/templates` |  | api\apps\canvas_app.py |

## 模块: /tenant_info

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/tenant_info` |  | api\apps\user_app.py |
| GET | `/tenant_info` |  | api\apps\user_app.py |

## 模块: /test_db_connect

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/test_db_connect` |  | api\apps\canvas_app.py |
| POST | `/test_db_connect` |  | api\apps\canvas_app.py |

## 模块: /test_mcp

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/test_mcp` |  | api\apps\mcp_server_app.py |
| POST | `/test_mcp` |  | api\apps\mcp_server_app.py |

## 模块: /test_tool

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/test_tool` |  | api\apps\mcp_server_app.py |
| POST | `/test_tool` |  | api\apps\mcp_server_app.py |

## 模块: /thumbnails

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/thumbnails` |  | api\apps\document_app.py |
| GET | `/thumbnails` |  | api\apps\document_app.py |

## 模块: /thumbup

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/thumbup` |  | api\apps\conversation_app.py |
| POST | `/thumbup` |  | api\apps\conversation_app.py |

## 模块: /token

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| DELETE | `/token/<token>` |  | api\apps\system_app.py |
| DELETE | `/token/<token>` |  | api\apps\system_app.py |

## 模块: /token_list

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/token_list` |  | api\apps\api_app.py |
| GET | `/token_list` |  | api\apps\api_app.py |
| GET | `/token_list` |  | api\apps\system_app.py |
| GET | `/token_list` |  | api\apps\system_app.py |

## 模块: /trace

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/trace` |  | api\apps\canvas_app.py |
| GET | `/trace` |  | api\apps\canvas_app.py |

## 模块: /trace_graphrag

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/trace_graphrag` |  | api\apps\kb_app.py |
| GET | `/trace_graphrag` |  | api\apps\kb_app.py |

## 模块: /trace_mindmap

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/trace_mindmap` |  | api\apps\kb_app.py |
| GET | `/trace_mindmap` |  | api\apps\kb_app.py |

## 模块: /trace_raptor

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/trace_raptor` |  | api\apps\kb_app.py |
| GET | `/trace_raptor` |  | api\apps\kb_app.py |

## 模块: /tts

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/tts` |  | api\apps\conversation_app.py |
| POST | `/tts` |  | api\apps\conversation_app.py |

## 模块: /unbind_task

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| DELETE | `/unbind_task` |  | api\apps\kb_app.py |
| DELETE | `/unbind_task` |  | api\apps\kb_app.py |

## 模块: /update

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/update` |  | api\apps\mcp_server_app.py |
| POST | `/update` |  | api\apps\mcp_server_app.py |

## 模块: /upload

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/upload/<canvas_id>` |  | api\apps\canvas_app.py |
| POST | `/upload/<canvas_id>` |  | api\apps\canvas_app.py |
| POST | `/upload` |  | api\apps\document_app.py |
| POST | `/upload` |  | api\apps\document_app.py |
| POST | `/upload` |  | api\apps\file_app.py |
| POST | `/upload` |  | api\apps\file_app.py |

## 模块: /upload_and_parse

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/upload_and_parse` |  | api\apps\document_app.py |
| POST | `/upload_and_parse` |  | api\apps\document_app.py |

## 模块: /users

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/users` |  | admin\server\routes.py |
| POST | `/users` |  | admin\server\routes.py |
| DELETE | `/users/<username>` |  | admin\server\routes.py |
| PUT | `/users/<username>/password` |  | admin\server\routes.py |
| PUT | `/users/<username>/activate` |  | admin\server\routes.py |
| GET | `/users/<username>` |  | admin\server\routes.py |
| GET | `/users/<username>/datasets` |  | admin\server\routes.py |
| GET | `/users/<username>/agents` |  | admin\server\routes.py |
| PUT | `/users/<user_name>/role` |  | admin\server\routes.py |
| GET | `/users/<user_name>/permission` |  | admin\server\routes.py |
| GET | `/users` |  | admin\server\routes.py |
| POST | `/users` |  | admin\server\routes.py |
| DELETE | `/users/<username>` |  | admin\server\routes.py |
| PUT | `/users/<username>/password` |  | admin\server\routes.py |
| PUT | `/users/<username>/activate` |  | admin\server\routes.py |
| GET | `/users/<username>` |  | admin\server\routes.py |
| GET | `/users/<username>/datasets` |  | admin\server\routes.py |
| GET | `/users/<username>/agents` |  | admin\server\routes.py |
| PUT | `/users/<user_name>/role` |  | admin\server\routes.py |
| GET | `/users/<user_name>/permission` |  | admin\server\routes.py |

## 模块: /version

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `/version` |  | api\apps\system_app.py |
| GET | `/version` |  | api\apps\system_app.py |

## 模块: /web_crawl

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| POST | `/web_crawl` |  | api\apps\document_app.py |
| POST | `/web_crawl` |  | api\apps\document_app.py |

## 模块: root

| 方法 | 端点 | 描述 | 控制器 |
|------|------|------|--------|
| GET | `error` |  | web\src\hooks\auth-hooks.ts |
| DELETE | `error` |  | web\src\hooks\auth-hooks.ts |
| GET | `auth` |  | web\src\hooks\auth-hooks.ts |
| DELETE | `auth` |  | web\src\hooks\auth-hooks.ts |
| GET | `auth` |  | web\src\hooks\auth-hooks.ts |
| GET | `auth` |  | web\src\hooks\auth-hooks.ts |
| GET | `folderId` |  | web\src\hooks\file-manager-hooks.ts |
| GET | `id` |  | web\src\hooks\knowledge-hooks.ts |
| GET | `page` |  | web\src\hooks\route-hook.ts |
| GET | `size` |  | web\src\hooks\route-hook.ts |
| GET | `page` |  | web\src\hooks\route-hook.ts |
| GET | `size` |  | web\src\hooks\route-hook.ts |
| GET | `shared_id` |  | web\src\hooks\use-agent-request.ts |
| GET | `folderId` |  | web\src\hooks\use-file-request.ts |
| GET | `id` |  | web\src\hooks\use-knowledge-request.ts |
| GET | `from` |  | web\src\pages\chat\shared-hooks.ts |
| GET | `shared_id` |  | web\src\pages\chat\shared-hooks.ts |
| GET | `locale` |  | web\src\pages\chat\shared-hooks.ts |
| GET | `visible_avatar` |  | web\src\pages\chat\shared-hooks.ts |
| GET | `visible_avatar` |  | web\src\pages\chat\shared-hooks.ts |
| GET | `id` |  | web\src\pages\dataflow-result\hooks.ts |
| GET | `id` |  | web\src\pages\dataflow-result\hooks.ts |
| GET | `folderId` |  | web\src\pages\file-manager\hooks.ts |
| GET | `folderId` |  | web\src\pages\files\hooks.ts |
| GET | `from` |  | web\src\pages\next-search\hooks.ts |
| GET | `shared_id` |  | web\src\pages\next-search\hooks.ts |
| GET | `locale` |  | web\src\pages\next-search\hooks.ts |
| GET | `tenantId` |  | web\src\pages\next-search\hooks.ts |
| GET | `visible_avatar` |  | web\src\pages\next-search\hooks.ts |
| GET | `visible_avatar` |  | web\src\pages\next-search\hooks.ts |
| GET | `shared_id` |  | web\src\pages\next-search\hooks.ts |
| GET | `shared_id` |  | web\src\pages\next-search\hooks.ts |
| GET | `shared_id` |  | web\src\pages\next-search\hooks.ts |
| GET | `shared_id` |  | web\src\pages\next-search\hooks.ts |
| GET | `shared_id` |  | web\src\pages\next-searches\hooks.ts |
| GET | `from` |  | web\src\pages\next-chats\hooks\use-send-shared-message.ts |
| GET | `shared_id` |  | web\src\pages\next-chats\hooks\use-send-shared-message.ts |
| GET | `locale` |  | web\src\pages\next-chats\hooks\use-send-shared-message.ts |
| GET | `visible_avatar` |  | web\src\pages\next-chats\hooks\use-send-shared-message.ts |
| GET | `visible_avatar` |  | web\src\pages\next-chats\hooks\use-send-shared-message.ts |
| GET | `id` |  | web\src\pages\dataset\dataset-overview\hook.ts |
| GET | `id` |  | web\src\pages\dataset\dataset-overview\hook.ts |
| GET | `from` |  | web\src\pages\agent\hooks\use-send-shared-message.ts |
| GET | `shared_id` |  | web\src\pages\agent\hooks\use-send-shared-message.ts |
| GET | `locale` |  | web\src\pages\agent\hooks\use-send-shared-message.ts |
| GET | `visible_avatar` |  | web\src\pages\agent\hooks\use-send-shared-message.ts |
| GET | `visible_avatar` |  | web\src\pages\agent\hooks\use-send-shared-message.ts |

## 外部API依赖

| 域名 | 基础URL | 用途 | 源文件 |
|------|---------|------|--------|
| github.com | `https://github.com` | 外部API调用 (get) | web\src\constants\agent.ts |
| example.com | `https://example.com` | 外部API调用 (get) | sandbox\tests\sandbox_security_tests_full.py |
| 127.0.0.1:61670 | `http://127.0.0.1:61670` | 外部API调用 (post) | rag\app\resume.py |
| open.feishu.cn | `https://open.feishu.cn` | 外部API调用 (get) | api\apps\user_app.py |
| api.example.com | `https://api.example.com` | 外部API调用 (GET) | .claude\skills\srs-reverse-engineering\scripts\discover_apis.py |
